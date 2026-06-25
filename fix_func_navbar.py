import re

try:
    with open('funcionalidades.html', 'r') as f:
        content = f.read()

    # 1. Replace the opening nav tag
    old_nav_start = '<nav class="navbar-shape shadow-lg">'
    new_nav_start = '''    <!-- Navbar -->
    <header id="main-header" class="fixed top-0 left-0 w-full flex justify-center z-50 transition-all duration-300 mt-4 px-3 md:px-0">
    <nav class="w-full max-w-[1200px] flex justify-between items-center px-5 md:px-8 py-3 md:py-4 bg-black/60 backdrop-blur-xl border border-white/10 rounded-[40px] shadow-2xl">'''
    content = content.replace(old_nav_start, new_nav_start)

    # 2. Replace the closing nav tag
    # The nav ends right before <!-- Hero Section -->
    old_nav_end = '''            </nav>

            


    <!-- Hero Section -->'''
    
    new_nav_end = '''            </nav>
    </header>

            


    <!-- Hero Section -->'''
    content = content.replace(old_nav_end, new_nav_end)
    
    # Wait, just in case the exact whitespace doesn't match:
    content = content.replace('</nav>\n\n            \n\n\n    <!-- Hero Section -->', '</nav>\n    </header>\n\n            \n\n\n    <!-- Hero Section -->')

    # 3. Add the JS scroll logic before the closing body tag
    scroll_js = '''
    <script>
        let lastScroll = 0;
        const header = document.getElementById('main-header');
        
        window.addEventListener('scroll', () => {
            const currentScroll = window.pageYOffset;
            
            if (currentScroll <= 0) {
                header.style.transform = 'translateY(0)';
                return;
            }
            
            if (currentScroll > lastScroll && currentScroll > 80) {
                // Scroll Down - hide header
                header.style.transform = 'translateY(-150%)';
            } else {
                // Scroll Up - show header
                header.style.transform = 'translateY(0)';
            }
            lastScroll = currentScroll;
        });
    </script>
</body>'''
    
    content = content.replace('</body>', scroll_js)

    with open('funcionalidades.html', 'w') as f:
        f.write(content)
        
except Exception as e:
    print(f"Error: {e}")
