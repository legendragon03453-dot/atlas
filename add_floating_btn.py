import re

def add_floating_button(content):
    floating_btn_html = """
    <!-- Botão Flutuante de Assinatura -->
    <div id="floating-cta" class="fixed bottom-6 lg:bottom-10 left-1/2 -translate-x-1/2 z-[90] transition-all duration-500 opacity-0 translate-y-10 pointer-events-none">
        <a href="#section-8" class="bg-atlas-red text-white hover:bg-atlas-red/90 shadow-[0_8px_32px_rgba(200,20,30,0.5)] py-3 px-8 rounded-full font-extrabold text-lg flex items-center justify-center gap-2 whitespace-nowrap pointer-events-auto border border-white/20 transition-transform hover:-translate-y-1 uppercase tracking-wide">
            <img src="https://github.com/legendragon03453-dot/atlas/blob/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp?raw=true" alt="Atlas" class="h-5 filter brightness-0 invert opacity-90 mt-[2px]">
            Assinar Atlas
        </a>
    </div>

    <script>
        document.addEventListener('DOMContentLoaded', function() {
            const floatingBtn = document.getElementById('floating-cta');
            const pricingSection = document.getElementById('section-8'); // Preços
            const footerSection = document.getElementById('main-footer'); // Or end of page
            
            window.addEventListener('scroll', () => {
                if (!floatingBtn) return;
                const scrollY = window.scrollY;
                
                // Mostra o botão depois de rolar a página (passando da Hero Section)
                let shouldShow = scrollY > window.innerHeight * 0.8;
                
                // Oculta o botão se já estiver na seção de Preços para não ficar redundante
                if (pricingSection) {
                    const pricingRect = pricingSection.getBoundingClientRect();
                    // Se a seção de preços estiver bem visível na tela
                    if (pricingRect.top < window.innerHeight && pricingRect.bottom > 0) {
                        shouldShow = false;
                    }
                }
                
                if (shouldShow) {
                    floatingBtn.classList.remove('opacity-0', 'translate-y-10', 'pointer-events-none');
                    floatingBtn.classList.add('opacity-100', 'translate-y-0');
                } else {
                    floatingBtn.classList.add('opacity-0', 'translate-y-10', 'pointer-events-none');
                    floatingBtn.classList.remove('opacity-100', 'translate-y-0');
                }
            });
        });
    </script>
</body>"""

    if "id=\"floating-cta\"" not in content:
        content = content.replace("</body>", floating_btn_html)
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = add_floating_button(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
