import re

def fix_js_toggle(filename):
    with open(filename, 'r') as f:
        content = f.read()

    js_fix = """
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
"""
    # Replace the existing script block
    pattern = re.compile(r'if\(menuBtn && menuOverlay\) \{.*?\}\n', re.DOTALL)
    if pattern.search(content):
        content = pattern.sub(js_fix, content, count=1)
    
    with open(filename, 'w') as f:
        f.write(content)

fix_js_toggle('index.html')
fix_js_toggle('funcionalidades.html')
