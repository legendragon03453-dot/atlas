import re
import os

def fix_all_links(content):
    # Início -> /
    content = re.sub(r'<a href="#" class="([^"]*)">Início</a>', r'<a href="/" class="\1">Início</a>', content)
    # A Metodologia -> /#section-7
    content = re.sub(r'<a href="#" class="([^"]*)">A Metodologia</a>', r'<a href="/#section-7" class="\1">A Metodologia</a>', content)
    # Preços -> /#section-8
    content = re.sub(r'<a href="#" class="([^"]*)">Preços</a>', r'<a href="/#section-8" class="\1">Preços</a>', content)
    # Dúvidas Frequentes -> /#section-9
    content = re.sub(r'<a href="#" class="([^"]*)">Dúvidas Frequentes</a>', r'<a href="/#section-9" class="\1">Dúvidas Frequentes</a>', content)
    return content

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        new_content = fix_all_links(content)
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Successfully processed {filename}")
        else:
            print(f"No changes made in {filename}")
            
    except FileNotFoundError:
        pass
