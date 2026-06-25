import re

def fix_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Ensure the #mobile-menu-btn CSS is robust
    css_fix = """
            #mobile-menu-btn {
                display: flex !important;
                flex-shrink: 0;
                visibility: visible !important;
                opacity: 1 !important;
                pointer-events: auto !important;
                z-index: 50;
            }
"""
    
    # Check if css_fix is already there or add it inside @media (max-width: 768px)
    if "#mobile-menu-btn {" not in content:
        # Find the @media (max-width: 768px) block and add the CSS
        content = re.sub(
            r'(@media\s*\(\s*max-width:\s*768px\s*\)\s*\{[^}]*navbar-shape\s*img\s*\{[^}]*\})',
            r'\1' + css_fix,
            content
        )
    else:
        # Replace existing #mobile-menu-btn CSS to be robust
        content = re.sub(
            r'#mobile-menu-btn\s*\{[^}]*\}',
            css_fix.strip(),
            content
        )

    # 2. Extract mobile-menu-overlay if it's inside footer and move it to before </body>
    overlay_match = re.search(r'(<div id="mobile-menu-overlay".*?</div>\s*</div>)', content, re.DOTALL)
    if overlay_match:
        overlay_html = overlay_match.group(1)
        # Remove it from current location
        content = content.replace(overlay_html, '')
        # Insert before <script> at the bottom or </body>
        # Wait, the regex might not capture the whole thing correctly. Let's do it carefully.
        
    # Actually, a better regex to extract the overlay:
    # It starts with <div id="mobile-menu-overlay" and ends with </div> just before the <script> or something.
    # Let's just find the start and balance the tags.
    
    # A simpler approach: Just find and replace the overlay using a known string pattern.
    pattern = re.compile(r'<!-- Menu Mobile Overlay -->.*?</nav>\s*</div>', re.DOTALL)
    overlay_match = pattern.search(content)
    if overlay_match:
        overlay_html = overlay_match.group(0)
        content = content.replace(overlay_html, '')
        # Add it right before </body>
        content = content.replace('</body>', overlay_html + '\n</body>')

    # 3. Update the JS to be robust
    # Instead of style.transform, let's toggle a class, or use style.transform but ensure the button works.
    js_fix = """
        // Mobile Menu Toggle (Robust Version)
        const menuBtn = document.getElementById('mobile-menu-btn');
        const menuClose = document.getElementById('mobile-menu-close');
        const menuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileLinks = document.querySelectorAll('.mobile-link');
        
        if(menuBtn && menuOverlay) {
            menuBtn.addEventListener('click', (e) => {
                e.preventDefault();
                menuOverlay.style.transform = 'translateY(0)';
                menuOverlay.style.visibility = 'visible';
                menuOverlay.style.opacity = '1';
            });
            menuClose.addEventListener('click', (e) => {
                e.preventDefault();
                menuOverlay.style.transform = 'translateY(-100%)';
            });
            mobileLinks.forEach(link => {
                link.addEventListener('click', () => {
                    menuOverlay.style.transform = 'translateY(-100%)';
                });
            });
        }
"""
    # Replace old JS
    content = re.sub(
        r'// Mobile Menu Toggle.*?if\(menuBtn && menuOverlay\) \{.*?\n\s*\}\n',
        js_fix,
        content,
        flags=re.DOTALL
    )

    with open(filename, 'w') as f:
        f.write(content)

fix_file('index.html')
fix_file('funcionalidades.html')
