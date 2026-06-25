import re

# Update index.html
with open('index.html', 'r') as f:
    index_content = f.read()

index_pattern = re.compile(r'<a href="#section-8" class="bg-\[#AFFF00\][^>]*>Teste 7 dias</a>\s*')
index_content = index_pattern.sub('', index_content)

with open('index.html', 'w') as f:
    f.write(index_content)


# Update funcionalidades.html
with open('funcionalidades.html', 'r') as f:
    func_content = f.read()

# Make sure overlay isn't already there somewhere hidden
if 'id="mobile-menu-overlay"' in func_content:
    # Remove any existing broken pieces of the overlay
    func_content = re.sub(r'<!-- Menu Mobile Overlay -->\s*(<div id="mobile-menu-overlay".*?</nav>\s*</div>)?', '', func_content, flags=re.DOTALL)

overlay_html = """
<!-- Menu Mobile Overlay -->
<div id="mobile-menu-overlay" class="fixed inset-0 bg-[#367CF5] z-[100] transform translate-y-[-100%] transition-transform duration-300 ease-in-out flex flex-col items-center justify-center">
    <button id="mobile-menu-close" class="absolute top-6 right-6 text-white p-2">
        <svg class="w-8 h-8" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"></path></svg>
    </button>
    <nav class="flex flex-col gap-6 text-white font-bold text-2xl text-center">
        <a href="/#section-7" class="mobile-link">Sobre</a>
        <a href="/#section-8" class="mobile-link">Preços</a>
        <a href="funcionalidades.html" class="mobile-link">Funcionalidades</a>
        <a href="/#section-9" class="mobile-link">FAQ</a>
        <a href="suporte.html" class="mobile-link">Suporte</a>
        <!-- CTA & Login -->
        <div class="flex flex-col items-center gap-3 mt-2">
            <a href="https://app.atlas.com.br" class="text-white/80 font-semibold text-base border border-white/30 px-8 py-3 rounded-full w-full text-center hover:bg-white/10 transition-colors">Entrar / Login</a>
        </div>
    </nav>
</div>
"""

func_content = func_content.replace('</body>', overlay_html + '\n</body>')

with open('funcionalidades.html', 'w') as f:
    f.write(func_content)
