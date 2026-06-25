import re

def fix_card_text_colors(content):
    # These text classes were conditionally white on desktop (md:) because the background was dark/transparent
    # Since background is now white globally, we remove the white text overrides
    
    # 1. Title text
    content = content.replace('md:text-white font-bold text-lg', 'font-bold text-lg')
    content = content.replace('text-gray-900 md:text-white', 'text-atlas-dark')
    
    # 2. Subtext (Sem Atlas)
    content = content.replace('text-gray-600 md:text-white/70', 'text-zinc-600')
    
    # 3. Subtext (Com Atlas)
    # The 'Com Atlas' text has:
    # <span class="text-atlas-blue md:text-[#36DCF5] font-bold text-[10px] tracking-wider uppercase">Com Atlas</span>
    content = content.replace('text-atlas-blue md:text-[#36DCF5]', 'text-atlas-blue')
    
    # Some other places might have md:text-white that we want to keep?
    # No, only in these cards we have "text-gray-600 md:text-white/70".
    # Wait, the h3 has `<h3 class="text-atlas-dark font-bold text-lg md:text-xl text-center md:text-left">O seu futuro</h3>` after the first replace above.
    
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_card_text_colors(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
