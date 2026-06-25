import re

def process_file(filename):
    with open(filename, 'r') as f:
        content = f.read()

    # 1. Replace the black square icon in buttons with the Atlas logo
    # `<div class="w-3 h-3 bg-black"></div>`
    # Let's be slightly flexible with spaces
    logo_img = '<img src="https://github.com/legendragon03453-dot/atlas/blob/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp?raw=true" alt="Atlas" class="h-4 md:h-5 filter brightness-0">'
    content = re.sub(r'<div class="w-3 h-3 bg-black"></div>', logo_img, content)

    # 2. Section 5 Cards adjustments for Mobile (white background, centered text, dark text colors)
    # The container of the cards is `div class="w-full max-w-5xl mx-auto flex flex-col gap-8 md:gap-12 relative z-10 mt-[-70vh] pb-[30vh]"`
    # But it's easier to just target the `card-3d-reveal` classes since they are unique to this section
    
    # Card wrapper
    content = content.replace('bg-white/10 backdrop-blur-md', 'bg-white md:bg-white/10 backdrop-blur-md border-gray-200 md:border-white/20')
    
    # Left Section (Icon + Title)
    # <div class="md:w-1/3 p-6 md:p-8 bg-white/5 flex items-center justify-center md:justify-start gap-4">
    content = content.replace('bg-white/5 flex items-center justify-center md:justify-start gap-4', 'bg-transparent md:bg-white/5 flex flex-col md:flex-row items-center justify-center md:justify-start gap-2 md:gap-4')
    
    # Lucide icons: <i data-lucide="rocket" class="w-6 h-6 text-white shrink-0"></i>
    content = re.sub(r'<i data-lucide="(.*?)" class="w-6 h-6 text-white shrink-0"></i>', r'<i data-lucide="\1" class="w-8 h-8 md:w-6 md:h-6 text-[#367CF5] md:text-white shrink-0 mb-1 md:mb-0"></i>', content)
    
    # Title: <h3 class="text-white font-bold text-lg md:text-xl text-center md:text-left">
    content = content.replace('<h3 class="text-white font-bold', '<h3 class="text-gray-900 md:text-white font-bold')
    
    # Middle Section (Sem Atlas)
    # <div class="flex-1 p-6 md:p-8 bg-white/5 flex flex-col justify-center items-start text-left border-l border-white/5">
    content = content.replace('bg-white/5 flex flex-col justify-center items-start text-left border-l border-white/5', 'bg-transparent md:bg-white/5 flex flex-col justify-center items-center md:items-start text-center md:text-left border-t md:border-t-0 border-l-0 md:border-l border-gray-100 md:border-white/5')
    
    # Text sem atlas: <p class="text-white/70 font-medium text-sm md:text-base leading-snug">
    content = content.replace('<p class="text-white/70 font-medium', '<p class="text-gray-600 md:text-white/70 font-medium')
    
    # Right Section (Com Atlas)
    # <div class="flex-1 p-6 md:p-8 bg-white/20 flex flex-col justify-center items-start text-left border-l border-white/5">
    content = content.replace('bg-white/20 flex flex-col justify-center items-start text-left border-l border-white/5', 'bg-blue-50 md:bg-white/20 flex flex-col justify-center items-center md:items-start text-center md:text-left border-t md:border-t-0 border-l-0 md:border-l border-gray-100 md:border-white/5')
    
    # Com Atlas badge text: <span class="text-[#36DCF5] font-bold text-[10px] tracking-wider uppercase">Com Atlas</span>
    # On white, #36DCF5 is invisible. Let's make it Atlas blue on mobile.
    content = content.replace('text-[#36DCF5] font-bold', 'text-[#367CF5] md:text-[#36DCF5] font-bold')
    
    # Text com atlas: <p class="text-white font-bold text-sm md:text-base leading-snug">
    content = content.replace('<p class="text-white font-bold', '<p class="text-gray-900 md:text-white font-bold')

    with open(filename, 'w') as f:
        f.write(content)

process_file('index.html')
try:
    process_file('funcionalidades.html')
except FileNotFoundError:
    pass
