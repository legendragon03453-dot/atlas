import re

def fix_timeline_colors(content):
    # Desktop version (floating on blue background)
    # old: <h3 class="text-atlas-dark font-bold text-[16px] md:text-xl mb-2 leading-tight">
    # new: <h3 class="text-white font-bold text-[16px] md:text-xl mb-2 leading-tight">
    content = content.replace('text-atlas-dark font-bold text-[16px] md:text-xl mb-2 leading-tight', 'text-white font-bold text-[16px] md:text-xl mb-2 leading-tight')
    
    # Also step 5 desktop:
    # old: <h3 class="text-atlas-dark font-bold text-[16px] md:text-xl mb-2 leading-tight">Você vê a vida inteira.<br>Começa a viver com propósito</h3>
    # The regex above handles this if the classes match perfectly.
    
    # Mobile version (inside white cards)
    # old: <h3 class="text-atlas-dark font-bold text-base mb-1 leading-snug">
    # new: <h3 class="text-atlas-blue font-bold text-base mb-1 leading-snug">
    content = content.replace('text-atlas-dark font-bold text-base mb-1 leading-snug', 'text-atlas-blue font-bold text-base mb-1 leading-snug')

    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_timeline_colors(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
