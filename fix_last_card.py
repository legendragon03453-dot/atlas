import re

def fix_last_card_text_color(content):
    # Change text-gray-600 to text-white/90 for the 5th card mobile text
    content = content.replace(
        '<p class="text-gray-600 md:text-white/75 text-sm leading-relaxed">Pensa em décadas. Sua vida financeira tem começo, meio e fim claro.</p>',
        '<p class="text-white/90 md:text-white/75 text-sm leading-relaxed">Pensa em décadas. Sua vida financeira tem começo, meio e fim claro.</p>'
    )
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_last_card_text_color(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
