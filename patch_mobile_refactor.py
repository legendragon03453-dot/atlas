import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Menu Mobile
old_menu_btn = """                <!-- Botão Teste Grátis -->
                <div class="flex-shrink-0 flex justify-end items-center">
                    <a href="#" class="btn-nav font-bold text-[13px] lg:text-[15px] flex items-center gap-2 whitespace-nowrap">
                        <svg width="10" height="10" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9.5 5.13397C10.1667 5.51887 10.1667 6.48113 9.5 6.86603L1.25 11.6292C0.583334 12.0141 -2.99723e-07 11.5329 -2.66089e-07 10.7631L1.50346e-07 1.23686C1.83981e-07 0.46706 0.583333 -0.0140645 1.25 0.370836L9.5 5.13397Z" fill="#1A2E44"/>
                        </svg>
                        <span class="hidden sm:inline">Começar</span><span class="sm:hidden">Start</span>
                    </a>
                </div>
            </nav>
        </header>"""

new_menu_btn = """                <!-- Botão Teste Grátis e Menu Mobile -->
                <div class="flex-shrink-0 flex justify-end items-center gap-2">
                    <a href="#" class="btn-nav font-bold text-[13px] lg:text-[15px] items-center gap-2 whitespace-nowrap hidden md:flex">
                        <svg width="10" height="10" viewBox="0 0 10 12" fill="none" xmlns="http://www.w3.org/2000/svg">
                            <path d="M9.5 5.13397C10.1667 5.51887 10.1667 6.48113 9.5 6.86603L1.25 11.6292C0.583334 12.0141 -2.99723e-07 11.5329 -2.66089e-07 10.7631L1.50346e-07 1.23686C1.83981e-07 0.46706 0.583333 -0.0140645 1.25 0.370836L9.5 5.13397Z" fill="#1A2E44"/>
                        </svg>
                        <span>Começar</span>
                    </a>
                    <button id="mobile-menu-btn" class="md:hidden flex items-center justify-center p-2 text-white/90">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path></svg>
                    </button>
                </div>
            </nav>
            
            <!-- Menu Mobile Overlay -->
            <div id="mobile-menu-overlay" class="fixed inset-0 bg-[#367CF5] z-[100] transform translate-y-[-100%] transition-transform duration-300 ease-in-out flex flex-col items-center justify-center">
                <button id="mobile-menu-close" class="absolute top-6 right-6 text-white p-2">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <nav class="flex flex-col gap-8 text-white font-bold text-2xl text-center">
                    <a href="#" class="mobile-link">Sobre</a>
                    <a href="#" class="mobile-link">Preços</a>
                    <a href="#" class="mobile-link">Funcionalidades</a>
                    <a href="#" class="mobile-link">FAQ</a>
                    <a href="#" class="btn-green text-[#1A2E05] px-8 py-3 rounded-full font-bold text-lg mt-4">Começar Agora</a>
                </nav>
            </div>
        </header>"""

content = content.replace(old_menu_btn, new_menu_btn)

# JS for Mobile Menu
mobile_js = """
            // Mobile Menu Toggle
            const menuBtn = document.getElementById('mobile-menu-btn');
            const menuClose = document.getElementById('mobile-menu-close');
            const menuOverlay = document.getElementById('mobile-menu-overlay');
            const mobileLinks = document.querySelectorAll('.mobile-link');
            
            if(menuBtn && menuOverlay) {
                menuBtn.addEventListener('click', () => {
                    menuOverlay.style.transform = 'translateY(0)';
                });
                menuClose.addEventListener('click', () => {
                    menuOverlay.style.transform = 'translateY(-100%)';
                });
                mobileLinks.forEach(link => {
                    link.addEventListener('click', () => {
                        menuOverlay.style.transform = 'translateY(-100%)';
                    });
                });
            }
"""
if "Mobile Menu Toggle" not in content:
    content = content.replace("// Mensal / Anual Toggle", mobile_js + "\n            // Mensal / Anual Toggle")

# 2. Section 2 (Orbit vs Grid)
old_circle = '<div class="circle-container">'
new_circle = """<div class="circle-container hidden md:block">"""
content = content.replace(old_circle, new_circle)

old_center = '<div class="center-box">'
new_center = '<div class="center-box hidden md:block">'
content = content.replace(old_center, new_center)

# Inject Mobile Grid right after circle-container div
orbit_html = """
            <div class="md:hidden grid grid-cols-2 gap-3 w-[90%] max-w-sm mt-8 pb-10">
                <!-- Mãe -->
                <div class="col-span-2 bg-[#0B1A30]/80 backdrop-blur-md border border-[#367CF5] p-5 rounded-xl text-center shadow-[0_0_15px_rgba(54,124,245,0.4)]">
                    <p class="text-white text-sm font-bold">Você não precisa ganhar mais.<br>Você precisa enxergar melhor.</p>
                </div>
                <!-- Filhas -->
                <div class="bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg">
                    <p class="text-white/90 text-xs font-medium leading-tight">Não tem noção do futuro</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg">
                    <p class="text-white/90 text-xs font-medium leading-tight">Vê o dinheiro entrar, mas não sobra</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg">
                    <p class="text-white/90 text-xs font-medium leading-tight">Quer guardar, mas não sabe como</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg">
                    <p class="text-white/90 text-xs font-medium leading-tight">Consome conteúdo, mas não age</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg">
                    <p class="text-white/90 text-xs font-medium leading-tight">Suas finanças estão espalhadas</p>
                </div>
                <div class="bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg">
                    <p class="text-white/90 text-xs font-medium leading-tight">Tem medo de investir errado</p>
                </div>
            </div>
"""
# insert before the snowball
content = content.replace('<!-- Bola Branca de Transição -->', orbit_html + '\n        <!-- Bola Branca de Transição -->')

# 3. Section 3 (Ordering & Padding)
# First card
content = content.replace('class="lg:absolute lg:left-4 xl:left-12 top-[15%] p-5 border border-white/30 rounded-lg w-[90%] max-w-[320px] lg:max-w-[280px] text-left mb-6 lg:mb-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30"',
                          'class="order-1 lg:order-none lg:absolute lg:left-4 xl:left-12 top-[15%] p-5 border border-white/30 rounded-lg w-[90%] max-w-[320px] lg:max-w-[280px] text-left mb-4 lg:mb-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30"')
# Image
content = content.replace('class="w-full max-w-3xl relative z-10 px-4"',
                          'class="w-full max-w-3xl relative z-10 px-4 order-3 lg:order-none mt-4 lg:mt-0"')
# Second card
content = content.replace('class="lg:absolute lg:right-4 xl:right-12 top-[15%] p-5 border border-white/30 rounded-lg w-[90%] max-w-[320px] lg:max-w-[280px] text-left mt-6 lg:mt-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30"',
                          'class="order-2 lg:order-none lg:absolute lg:right-4 xl:right-12 top-[15%] p-5 border border-white/30 rounded-lg w-[90%] max-w-[320px] lg:max-w-[280px] text-left mt-0 lg:mt-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30"')

# Remove base gap (Section 4 padding/margin adjust)
content = content.replace('<section id="section-4" class="w-full bg-[#367CF5] flex flex-col items-center pt-16 pb-20 md:pt-24 md:pb-32 relative overflow-hidden">',
                          '<section id="section-4" class="w-full bg-[#367CF5] flex flex-col items-center pt-2 md:pt-24 pb-20 md:pb-32 relative overflow-hidden -mt-10 lg:mt-0">')
content = content.replace('class="bg-[#f0f2f5] p-8 md:p-12 rounded-2xl max-w-3xl w-[90%] mx-auto text-center relative z-10 shadow-sm -mt-8 md:-mt-16 lg:-mt-24"',
                          'class="bg-[#f0f2f5] p-8 md:p-12 rounded-2xl max-w-3xl w-[90%] mx-auto text-center relative z-10 shadow-sm -mt-16 md:-mt-16 lg:-mt-24"')

# 4. Section 4 Timeline Direct (Head | Paragraph)
# Hide the complex timeline on mobile
content = content.replace('class="relative w-full max-w-5xl h-[900px] md:h-[1200px] lg:h-[1600px] mx-auto mt-10"',
                          'class="relative w-full max-w-5xl h-[900px] md:h-[1200px] lg:h-[1600px] mx-auto mt-10 hidden md:block"')

# Add direct timeline for mobile
mobile_timeline = """
        <!-- Timeline Direta Mobile -->
        <div class="md:hidden flex flex-col gap-6 w-[90%] mx-auto mt-8 relative z-20">
            <div class="grid grid-cols-[1fr_2fr] gap-4 items-center bg-[#2968DF]/30 p-4 rounded-xl border border-white/10">
                <h3 class="text-white font-bold text-sm leading-tight border-r border-white/20 pr-3">Você vê o que aconteceu.</h3>
                <p class="text-white/80 text-xs leading-relaxed">Você registra o mês, vê onde o dinheiro foi.</p>
            </div>
            <div class="grid grid-cols-[1fr_2fr] gap-4 items-center bg-[#2968DF]/30 p-4 rounded-xl border border-white/10">
                <h3 class="text-white font-bold text-sm leading-tight border-r border-white/20 pr-3">Você categoriza.</h3>
                <p class="text-white/80 text-xs leading-relaxed">Cada categoria revela um valor seu. Alinha gastos.</p>
            </div>
            <div class="grid grid-cols-[1fr_2fr] gap-4 items-center bg-[#2968DF]/30 p-4 rounded-xl border border-white/10">
                <h3 class="text-white font-bold text-sm leading-tight border-r border-white/20 pr-3">Você projeta.</h3>
                <p class="text-white/80 text-xs leading-relaxed">Sai do presente e entra no futuro. Meta tangível.</p>
            </div>
            <div class="grid grid-cols-[1fr_2fr] gap-4 items-center bg-[#2968DF]/30 p-4 rounded-xl border border-white/10">
                <h3 class="text-white font-bold text-sm leading-tight border-r border-white/20 pr-3">Decide com dados.</h3>
                <p class="text-white/80 text-xs leading-relaxed">Vê o impacto de cada escolha. R$100 a mais em 20 anos.</p>
            </div>
            <div class="grid grid-cols-[1fr_2fr] gap-4 items-center bg-[#2968DF]/30 p-4 rounded-xl border border-white/10">
                <h3 class="text-white font-bold text-sm leading-tight border-r border-white/20 pr-3">Vê a vida inteira.</h3>
                <p class="text-white/80 text-xs leading-relaxed">Uma história com começo, meio e fim claro.</p>
            </div>
        </div>
"""
content = content.replace('<!-- Título -->', mobile_timeline + '\n        <!-- Título -->')


# 5. Section 6 Yin-Yang Comparison
# In Section 5 (Tabela de Comparação), the cards are Sem/Com Atlas.
# Current: class="grid gap-6 grid-cols-1 md:grid-cols-2 max-w-5xl mx-auto w-full relative z-10"
# New: class="grid gap-2 sm:gap-6 grid-cols-2 md:grid-cols-2 max-w-5xl mx-auto w-full relative z-10 px-1 sm:px-4"
content = content.replace('class="grid gap-6 grid-cols-1 md:grid-cols-2 max-w-5xl mx-auto w-full relative z-10"',
                          'class="grid gap-1 md:gap-6 grid-cols-2 md:grid-cols-2 max-w-5xl mx-auto w-[98%] sm:w-full relative z-10"')

# Reduzir padding dos cards para caber
content = content.replace('class="bg-white/5 border border-white/10 rounded-2xl p-8 md:p-12 flex flex-col justify-between"',
                          'class="bg-white/5 border border-white/10 rounded-xl md:rounded-2xl p-4 md:p-12 flex flex-col justify-between"')
content = content.replace('class="bg-gradient-to-b from-[#A3E635] to-[#76CC00] rounded-2xl p-8 md:p-12 text-[#1A2E05] flex flex-col justify-between relative overflow-hidden shadow-[0_0_40px_rgba(163,230,53,0.3)]"',
                          'class="bg-gradient-to-b from-[#A3E635] to-[#76CC00] rounded-xl md:rounded-2xl p-4 md:p-12 text-[#1A2E05] flex flex-col justify-between relative overflow-hidden shadow-[0_0_40px_rgba(163,230,53,0.3)]"')

# Ajustar tamanho das fontes dentro dos cards
content = content.replace('<h3 class="text-2xl md:text-3xl font-bold mb-8">Sem Atlas</h3>',
                          '<h3 class="text-base md:text-3xl font-bold mb-4 md:mb-8 text-center md:text-left">Sem Atlas</h3>')
content = content.replace('<h3 class="text-2xl md:text-3xl font-bold mb-8 relative z-10">Com Atlas</h3>',
                          '<h3 class="text-base md:text-3xl font-bold mb-4 md:mb-8 relative z-10 text-center md:text-left">Com Atlas</h3>')

# Ajustar o SVG check e cross
content = content.replace('<svg class="w-6 h-6 shrink-0 text-red-400 mt-1"', '<svg class="w-4 h-4 md:w-6 md:h-6 shrink-0 text-red-400 mt-1 md:mt-1"')
content = content.replace('<svg class="w-6 h-6 shrink-0 text-[#1A2E05] mt-1"', '<svg class="w-4 h-4 md:w-6 md:h-6 shrink-0 text-[#1A2E05] mt-1 md:mt-1"')

# Ajustar texto da lista
content = content.replace('<span class="text-white/80 font-medium">', '<span class="text-white/80 font-medium text-xs md:text-base leading-tight md:leading-normal">')
content = content.replace('<span class="font-bold">', '<span class="font-bold text-xs md:text-base leading-tight md:leading-normal">')

# Ajustar gaps da lista
content = content.replace('<ul class="space-y-6">', '<ul class="space-y-4 md:space-y-6">')
content = content.replace('<ul class="space-y-6 relative z-10">', '<ul class="space-y-4 md:space-y-6 relative z-10">')

# Esconder button grande do Com Atlas no mobile para economizar espaço
content = content.replace('class="bg-[#1A2E05] text-white px-8 py-4 rounded-xl font-bold mt-12 text-center relative z-10 w-full flex items-center justify-center gap-3 transition-transform hover:-translate-y-1 shadow-lg"',
                          'class="bg-[#1A2E05] text-white px-4 py-2 md:px-8 md:py-4 rounded-xl font-bold mt-6 md:mt-12 text-center relative z-10 w-full hidden md:flex items-center justify-center gap-3 transition-transform hover:-translate-y-1 shadow-lg"')

with open(filepath, 'w') as f:
    f.write(content)

