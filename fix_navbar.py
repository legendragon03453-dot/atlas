import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove the custom .navbar-shape CSS
content = re.sub(r'\.navbar-shape\s*{[^}]*}\s*@media[^{]*{[^{]*\.[^{]*{[^}]*}[^}]*}', '', content, flags=re.DOTALL)

# 2. Rewrite the header HTML
new_header = """<header id="main-header" class="fixed top-0 left-0 w-full z-50 transition-all duration-300">
    <div class="w-full flex justify-center bg-black/80 md:bg-transparent backdrop-blur-lg md:backdrop-blur-none border-b border-white/10 md:border-none">
        <nav class="w-full max-w-[1200px] flex justify-between items-center px-4 md:px-8 py-3 md:py-4 md:mt-4 md:bg-black/60 md:backdrop-blur-xl md:border md:border-white/10 md:rounded-[40px] shadow-lg">"""

pattern = re.compile(r'<header id="main-header"[^>]*>\s*<nav class="navbar-shape shadow-lg">', re.DOTALL)
content = pattern.sub(new_header, content)

# 3. Ensure the mobile menu btn SVG is visible
# It currently is `<svg class="w-6 h-6"...>` it's fine.

with open('index.html', 'w') as f:
    f.write(content)

with open('funcionalidades.html', 'r') as f:
    f_content = f.read()

# Also do the same for funcionalidades.html just to be safe
f_content = re.sub(r'\.navbar-shape\s*{[^}]*}\s*@media[^{]*{[^{]*\.[^{]*{[^}]*}[^}]*}', '', f_content, flags=re.DOTALL)
f_content = pattern.sub(new_header, f_content)

with open('funcionalidades.html', 'w') as f:
    f_content = f.write(f_content)
