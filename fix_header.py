import re

with open('index.html', 'r') as f:
    content = f.read()

# Make header fixed
old_header = '<header style="width: 100%; position: absolute; height: 70px; z-index: 50; top: 0;">'
new_header = '<header id="main-header" style="width: 100%; position: fixed; height: 70px; z-index: 50; top: 0; transition: all 0.3s ease;">'
content = content.replace(old_header, new_header)

# Make navbar more rounded
old_nav = '<nav class="navbar-shape shadow-lg">'
new_nav = '<nav class="navbar-shape shadow-lg" style="border-radius: 40px;">'
content = content.replace(old_nav, new_nav)

# Add "Entrar" and hide "Teste 7 dias"
# The current buttons container:
old_buttons = """                            <!-- Botão Teste Grátis -->
            <div class="flex-shrink-0 flex justify-end items-center gap-2">
                <a href="#" class="btn-nav font-bold text-[13px] lg:text-[15px] items-center gap-2 whitespace-nowrap hidden md:flex">
                    <svg width="10" height="10" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.5 5.13397C10.1667 5.51887 10.1667 6.48113 9.5 6.86603L1.25 11.6292C0.583334 12.0141 -2.99723e-07 11.5329 -2.66089e-07 10.7631L1.50346e-07 1.23686C1.83981e-07 0.46706 0.583333 -0.0140645 1.25 0.370836L9.5 5.13397Z" fill="#1A2E44"/>
                    </svg>
                    <span>Teste 7 dias</span>
                </a>
                <button id="mobile-menu-btn" class="md:hidden flex items-center justify-center p-2 text-white/90">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
            </div>"""

new_buttons = """                            <!-- Botões da Direita -->
            <div class="flex-shrink-0 flex justify-end items-center gap-3">
                <a href="https://app.atlas.com.br" class="text-white font-medium text-[14px] lg:text-[16px] hover:text-blue-200 transition-colors hidden md:block">Entrar</a>
                
                <a href="#section-8" id="nav-cta-btn" class="bg-[#AFFF00] text-[#1A2E05] px-6 py-2 rounded-full font-bold text-[13px] lg:text-[15px] items-center gap-2 whitespace-nowrap hidden md:flex opacity-0 transition-opacity duration-300 pointer-events-none hover:bg-[#9add00]">
                    <svg width="10" height="10" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                        <path d="M9.5 5.13397C10.1667 5.51887 10.1667 6.48113 9.5 6.86603L1.25 11.6292C0.583334 12.0141 -2.99723e-07 11.5329 -2.66089e-07 10.7631L1.50346e-07 1.23686C1.83981e-07 0.46706 0.583333 -0.0140645 1.25 0.370836L9.5 5.13397Z" fill="#1A2E05"/>
                    </svg>
                    <span>Teste 7 dias</span>
                </a>
                <button id="mobile-menu-btn" class="md:hidden flex items-center justify-center p-2 text-white/90">
                    <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                </button>
            </div>"""

content = content.replace(old_buttons, new_buttons)

with open('index.html', 'w') as f:
    f.write(content)

