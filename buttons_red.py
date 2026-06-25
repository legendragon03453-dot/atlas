import re

def change_buttons_to_red(content):
    # 1. Hero / Section buttons (btn-green)
    content = content.replace('class="btn-green text-[#1A2E05]', 'class="bg-atlas-red text-white hover:bg-atlas-red/90 shadow-lg')
    # If any generic btn-green exist
    content = content.replace('btn-green', 'bg-atlas-red text-white hover:bg-atlas-red/90')

    # 2. Pricing table buttons
    # Essencial and Elite
    content = content.replace('bg-[#0B1A30] text-white font-bold hover:bg-[#1a2e4f]', 'bg-atlas-red text-white font-bold hover:bg-atlas-red/90')
    # Pro
    content = content.replace('bg-[#A3E635] text-atlas-dark font-extrabold hover:bg-[#8cdc18]', 'bg-atlas-red text-white font-extrabold hover:bg-atlas-red/90')

    # 3. Teste Grátis button
    # Old: bg-gradient-to-r from-[#AFFF00] via-[#8cdc18] to-[#AFFF00] bg-[length:200%_auto] text-[#1A2E05]
    content = re.sub(
        r'bg-gradient-to-r from-\[#AFFF00\] via-\[#8cdc18\] to-\[#AFFF00\] bg-\[length:200%_auto\] text-\[#1A2E05\]',
        r'bg-atlas-red text-white hover:bg-atlas-red/90',
        content
    )

    # 4. Login button in funcionalidades.html
    # Old: bg-atlas-blue hover:bg-atlas-blue text-white
    content = content.replace('bg-atlas-blue hover:bg-atlas-blue text-white', 'bg-atlas-red hover:bg-atlas-red/90 text-white')
    
    # Let's make sure the logo button doesn't get messed up if it has something similar (it doesn't).
    
    return content

files = ['index.html', 'funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = change_buttons_to_red(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
