import re

def fix_broken_css_and_gsap(content):
    # 1. Fix the broken CSS block
    broken_css_pattern = r'/\*\s*Estilos do Botão Verde\s*\*/\s*\.bg-atlas-red text-white hover:bg-atlas-red/90\s*\{[^}]+\}\s*\.bg-atlas-red text-white hover:bg-atlas-red/90:hover\s*\{[^}]+\}'
    fixed_css = '''/* Estilos do Botão Hero */
        .hero-cta {
            transition: transform 0.2s, box-shadow 0.2s;
        }
        
        .hero-cta:hover {
            transform: translateY(-2px);
            box-shadow: 0px 6px 20px rgba(184, 43, 38, 0.4);
        }'''
    content = re.sub(broken_css_pattern, fixed_css, content, flags=re.MULTILINE)
    
    # 2. Fix the broken GSAP selector
    content = content.replace('".bg-atlas-red text-white hover:bg-atlas-red/90"', '".hero-cta"')
    
    # 3. Add ' hero-cta' to the hero buttons so they can be targeted
    content = content.replace('class="bg-atlas-red text-white hover:bg-atlas-red/90 shadow-lg', 'class="bg-atlas-red text-white hover:bg-atlas-red/90 shadow-lg hero-cta')

    # Also fix it in case it was applied somewhere else
    # Let's reduce the button size slightly if the user complained it's too big:
    # From: md:px-28 md:py-8 text-2xl md:text-5xl
    # To: md:px-20 md:py-6 text-xl md:text-4xl
    content = content.replace('md:px-28 md:py-8 rounded-full font-black text-2xl md:text-5xl', 'md:px-20 md:py-6 rounded-full font-black text-xl md:text-4xl')
    
    return content

files = ['index.html', 'funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_broken_css_and_gsap(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
