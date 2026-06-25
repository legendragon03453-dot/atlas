import re

new_header = """<header id="main-header" class="fixed top-0 w-full flex justify-center z-[99] transition-all duration-300 mt-4 px-3 md:px-0">
    <nav class="w-full max-w-[1200px] flex justify-between items-center px-5 md:px-8 py-3 md:py-4 bg-black/60 backdrop-blur-xl border border-white/10 rounded-[40px] shadow-2xl">
        <!-- Logo -->
        <div class="flex-shrink-0 flex justify-start items-center">
            <a href="/">
                <img src="https://github.com/legendragon03453-dot/atlas/blob/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp?raw=true" alt="Atlas Logo" class="h-8 md:h-10">
            </a>
        </div>

        <!-- Links de Navegação -->
        <div class="nav-links flex-1 hidden md:flex justify-center items-center gap-4 lg:gap-8 text-white font-medium text-[14px] lg:text-[16px] whitespace-nowrap px-4">
            <a href="#section-7" class="hover:text-blue-200 transition-colors">Sobre</a>
            <a href="#section-8" class="hover:text-blue-200 transition-colors">Preços</a>
            <a href="funcionalidades.html" class="hover:text-blue-200 transition-colors">Funcionalidades</a>
            <a href="#section-9" class="hover:text-blue-200 transition-colors">FAQ</a>
            <a href="suporte.html" class="hover:text-blue-200 transition-colors">Suporte</a>
        </div>

        <!-- Botões da Direita -->
        <div class="flex-shrink-0 flex justify-end items-center gap-3">
            <a href="https://app.useatlasapp.com/auth" class="text-white font-medium text-[14px] lg:text-[16px] hover:text-blue-200 transition-colors hidden md:block">Entrar</a>
            
            <button id="mobile-menu-btn" class="md:hidden flex items-center justify-center p-2 text-white/90 focus:outline-none cursor-pointer z-[100] relative">
                <svg class="w-7 h-7" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
            </button>
        </div>
    </nav>
</header>"""

for filename in ['index.html', 'funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()

    # Find the current header block
    pattern = re.compile(r'<header id="main-header".*?</header>', re.DOTALL)
    content = pattern.sub(new_header, content)

    with open(filename, 'w') as f:
        f.write(content)
