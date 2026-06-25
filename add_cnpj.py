import re
import os

def add_cnpj_to_footer(content):
    target = """<p class="text-sm text-white/60">
                        &copy; 2026 Atlas. Todos os direitos reservados.
                    </p>"""
                    
    replacement = """<p class="text-sm text-white/60">
                        &copy; 2026 Atlas. Todos os direitos reservados.
                    </p>
                    <p class="text-xs text-white/50 mt-1">
                        CNPJ: 59.816.277/0001-30
                    </p>"""
    
    if target in content:
        return content.replace(target, replacement)
    else:
        # Regex fallback just in case formatting is slightly different
        return re.sub(
            r'<p class="text-sm text-white/60">\s*&copy; 2026 Atlas. Todos os direitos reservados.\s*</p>',
            replacement,
            content,
            flags=re.DOTALL
        )

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        new_content = add_cnpj_to_footer(content)
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Successfully processed {filename}")
        else:
            print(f"No changes made in {filename}")
            
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
