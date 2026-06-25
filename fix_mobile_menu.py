import re

def fix_mobile_menu_script(content):
    target = """<script>

        
        // Mobile Menu Toggle (Robust Version)
        const menuBtn = document.getElementById('mobile-menu-btn');
        const menuClose = document.getElementById('mobile-menu-close');
        const menuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileLinks = document.querySelectorAll('.mobile-link');
        
        
        if(menuBtn && menuOverlay) {
            menuBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                menuOverlay.classList.remove('translate-y-[-100%]');
                menuOverlay.classList.add('translate-y-0');
                // Remove any inline styles if they were set previously
                menuOverlay.style.transform = '';
            });
            menuClose.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                menuOverlay.classList.remove('translate-y-0');
                menuOverlay.classList.add('translate-y-[-100%]');
                menuOverlay.style.transform = '';
            });
            mobileLinks.forEach(link => {
                link.addEventListener('click', () => {
                    menuOverlay.classList.remove('translate-y-0');
                    menuOverlay.classList.add('translate-y-[-100%]');
                    menuOverlay.style.transform = '';
                });
            });
        }

</script>"""

    replacement = """<script>
    document.addEventListener("DOMContentLoaded", function() {
        // Mobile Menu Toggle (Robust Version)
        const menuBtn = document.getElementById('mobile-menu-btn');
        const menuClose = document.getElementById('mobile-menu-close');
        const menuOverlay = document.getElementById('mobile-menu-overlay');
        const mobileLinks = document.querySelectorAll('.mobile-link');
        
        if(menuBtn && menuOverlay) {
            menuBtn.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                menuOverlay.classList.remove('translate-y-[-100%]');
                menuOverlay.classList.add('translate-y-0');
                menuOverlay.style.transform = '';
            });
            menuClose.addEventListener('click', (e) => {
                e.preventDefault();
                e.stopPropagation();
                menuOverlay.classList.remove('translate-y-0');
                menuOverlay.classList.add('translate-y-[-100%]');
                menuOverlay.style.transform = '';
            });
            mobileLinks.forEach(link => {
                link.addEventListener('click', () => {
                    menuOverlay.classList.remove('translate-y-0');
                    menuOverlay.classList.add('translate-y-[-100%]');
                    menuOverlay.style.transform = '';
                });
            });
        }
    });
</script>"""
    
    if target in content:
        content = content.replace(target, replacement)
    else:
        print("Target not found exactly, using regex")
        # Regex fallback just in case spaces/newlines differ
        content = re.sub(
            r'<script>\s*// Mobile Menu Toggle \(Robust Version\).*?</script>',
            replacement,
            content,
            flags=re.DOTALL
        )
    return content

files = ['funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_mobile_menu_script(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
