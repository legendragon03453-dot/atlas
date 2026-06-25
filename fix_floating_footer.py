import re

def fix_floating_button_footer(content):
    target = """                if (pricingSection) {
                    const pricingRect = pricingSection.getBoundingClientRect();
                    // Se a seção de preços estiver bem visível na tela
                    if (pricingRect.top < window.innerHeight && pricingRect.bottom > 0) {
                        shouldShow = false;
                    }
                }"""
                
    replacement = """                if (pricingSection) {
                    const pricingRect = pricingSection.getBoundingClientRect();
                    // Se a seção de preços estiver bem visível na tela
                    if (pricingRect.top < window.innerHeight && pricingRect.bottom > 0) {
                        shouldShow = false;
                    }
                }
                
                // Oculta se o footer estiver na tela para não colidir
                const footerEl = document.querySelector('footer');
                if (footerEl) {
                    const footerRect = footerEl.getBoundingClientRect();
                    if (footerRect.top < window.innerHeight) {
                        shouldShow = false;
                    }
                }"""
    
    if target in content:
        content = content.replace(target, replacement)
    else:
        print("Target block not found, trying regex...")
        content = re.sub(
            r'if \(pricingSection\) \{.*?\}',
            replacement,
            content,
            flags=re.DOTALL
        )
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_floating_button_footer(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
