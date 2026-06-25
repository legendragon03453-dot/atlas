import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Menu Mobile Insertion (with correct match)
old_header_end = re.search(r'<!-- Botão Teste Grátis -->.*?Teste por 7 dias grátis.*?</a>.*?</div>.*?</nav>.*?</header>', content, re.DOTALL)
if old_header_end:
    new_header_end = """                <!-- Botão Teste Grátis -->
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
                </div>
            </nav>
            
            <!-- Menu Mobile Overlay -->
            <div id="mobile-menu-overlay" class="fixed inset-0 bg-[#367CF5] z-[100] transform translate-y-[100%] transition-transform duration-300 ease-in-out flex flex-col items-center justify-center pointer-events-none opacity-0">
                <button id="mobile-menu-close" class="absolute top-6 right-6 text-white p-2 pointer-events-auto">
                    <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
                </button>
                <nav class="flex flex-col gap-8 text-white font-bold text-2xl text-center pointer-events-auto">
                    <a href="#section-7" class="mobile-link">Sobre</a>
                    <a href="#section-8" class="mobile-link">Preços</a>
                    <a href="#" class="mobile-link">Funcionalidades</a>
                    <a href="#section-9" class="mobile-link">FAQ</a>
                    <a href="#" class="mobile-link">Suporte</a>
                    <a href="#" class="btn-green text-[#1A2E05] px-8 py-3 rounded-full font-bold text-lg mt-4 text-center justify-center">Começar Agora</a>
                </nav>
            </div>
        </header>"""
    content = content.replace(old_header_end.group(0), new_header_end)

# JS for Mobile Menu (with opacity/pointer-events fix)
mobile_js = """
            // Mobile Menu Toggle
            const menuBtn = document.getElementById('mobile-menu-btn');
            const menuClose = document.getElementById('mobile-menu-close');
            const menuOverlay = document.getElementById('mobile-menu-overlay');
            const mobileLinks = document.querySelectorAll('.mobile-link');
            
            if(menuBtn && menuOverlay) {
                menuBtn.addEventListener('click', () => {
                    menuOverlay.style.transform = 'translateY(0)';
                    menuOverlay.style.opacity = '1';
                    menuOverlay.style.pointerEvents = 'auto';
                });
                const closeMenu = () => {
                    menuOverlay.style.transform = 'translateY(100%)';
                    menuOverlay.style.opacity = '0';
                    menuOverlay.style.pointerEvents = 'none';
                };
                menuClose.addEventListener('click', closeMenu);
                mobileLinks.forEach(link => {
                    link.addEventListener('click', closeMenu);
                });
            }
"""
if "Mobile Menu Toggle" not in content:
    content = content.replace("// Mensal / Anual Toggle", mobile_js + "\n            // Mensal / Anual Toggle")

# 2. Add Suporte to Desktop Navbar and set hrefs
content = content.replace('<a href="#" class="hover:text-blue-200 transition-colors">Sobre</a>', '<a href="#section-7" class="hover:text-blue-200 transition-colors">Sobre</a>')
content = content.replace('<a href="#" class="hover:text-blue-200 transition-colors">Preços</a>', '<a href="#section-8" class="hover:text-blue-200 transition-colors">Preços</a>')
# Add FAQ link just in case
content = content.replace('<a href="#" class="hover:text-blue-200 transition-colors">FAQ</a>', '<a href="#section-9" class="hover:text-blue-200 transition-colors">FAQ</a>\n                    <a href="#" class="hover:text-blue-200 transition-colors">Suporte</a>')

# 3. Add Suporte to Footer
# Find: <a href="#" class="hover:text-white transition-colors">Dúvidas Frequentes</a>
old_footer_link = '<a href="#" class="hover:text-white transition-colors">Dúvidas Frequentes</a>'
new_footer_link = '<a href="#" class="hover:text-white transition-colors">Dúvidas Frequentes</a>\n                <a href="#" class="hover:text-white transition-colors">Suporte</a>'
content = content.replace(old_footer_link, new_footer_link)

with open(filepath, 'w') as f:
    f.write(content)

