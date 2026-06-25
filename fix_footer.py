import re
import os

def fix_footer_links(content):
    target_block = """<nav class="mb-4 flex flex-wrap justify-center gap-6 lg:gap-10 text-white/90 font-medium text-sm md:text-base">
                    <a href="#" class="hover:text-white transition-colors">Início</a>
                    <a href="#" class="hover:text-white transition-colors">A Metodologia</a>
                    <a href="#" class="hover:text-white transition-colors">Preços</a>
                    <a href="funcionalidades.html" class="hover:text-white transition-colors">Funcionalidades</a>
                    <a href="#" class="hover:text-white transition-colors">Dúvidas Frequentes</a>
                    <a href="suporte.html" class="hover:text-white transition-colors">Suporte</a>
                </nav>"""
                
    replacement_block = """<nav class="mb-4 flex flex-wrap justify-center gap-6 lg:gap-10 text-white/90 font-medium text-sm md:text-base">
                    <a href="/" class="hover:text-white transition-colors">Início</a>
                    <a href="/#section-7" class="hover:text-white transition-colors">A Metodologia</a>
                    <a href="/#section-8" class="hover:text-white transition-colors">Preços</a>
                    <a href="funcionalidades.html" class="hover:text-white transition-colors">Funcionalidades</a>
                    <a href="/#section-9" class="hover:text-white transition-colors">Dúvidas Frequentes</a>
                    <a href="suporte.html" class="hover:text-white transition-colors">Suporte</a>
                </nav>"""
    
    if target_block in content:
        return content.replace(target_block, replacement_block)
    else:
        # Regex fallback
        return re.sub(
            r'<nav class="mb-4 flex flex-wrap justify-center.*?Início.*?A Metodologia.*?Preços.*?</nav>',
            replacement_block,
            content,
            flags=re.DOTALL
        )

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        new_content = fix_footer_links(content)
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Successfully processed {filename}")
        else:
            print(f"No changes made in {filename}")
            
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
