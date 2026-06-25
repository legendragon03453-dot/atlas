import os
import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update the Google Fonts link
old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800;900&family=Playfair+Display:ital,wght@0,400;0,500;0,600;0,700;1,400;1,500;1,600;1,700&display=swap" rel="stylesheet">'
if old_fonts in content:
    content = content.replace(old_fonts, new_fonts)
else:
    # If already replaced or slightly different, try regex
    content = re.sub(r'<link href="https://fonts.googleapis.com/css2\?family=Inter[^"]+" rel="stylesheet">', new_fonts, content)

# 2. Add custom class for the elegant serif font
style_tag_end = content.find('</style>')
if style_tag_end != -1 and '.font-playfair' not in content:
    custom_classes = """
        .font-playfair {
            font-family: 'Playfair Display', serif;
        }
"""
    content = content[:style_tag_end] + custom_classes + content[style_tag_end:]

# 3. Replace 'font-serif' with 'font-playfair' in the existing Section 6
content = content.replace('font-normal italic font-serif', 'font-normal italic font-playfair')

# 4. Update Section 1
old_s1 = 'Não tente adivinhar seu futuro financeiro. Construa um mapa.'
new_s1 = 'Não tente adivinhar seu futuro financeiro. <span class="font-normal italic font-playfair text-[#84cc16]">Construa um mapa.</span>'
content = content.replace(old_s1, new_s1)

# 5. Update Section 2 (Toda montanha precisa de um caminho)
old_s2 = 'Toda montanha precisa<br>de um <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-[#A3E635] inline-block pb-2 animate-gradient-x">caminho</span>'
# Wait, the word "caminho" is animated with a gradient. We can keep the gradient and just add the font-playfair
new_s2 = 'Toda montanha precisa<br>de um <span class="text-transparent bg-clip-text bg-gradient-to-r from-blue-400 to-[#A3E635] inline-block pb-2 animate-gradient-x font-normal italic font-playfair">caminho</span>'
content = content.replace(old_s2, new_s2)

# 6. Update Section 3
old_s3 = """        <!-- Header Centralizado -->
        <h2 class="text-center text-3xl md:text-5xl font-bold text-[#1a1a1a] mb-12 lg:mb-20 tracking-tight leading-tight relative z-20">
            Não é mais um app de controle.<br>
            É um mapa do seu futuro.
        </h2>"""
new_s3 = """        <!-- Header Centralizado -->
        <h2 class="text-center text-3xl md:text-5xl font-bold text-[#1a1a1a] mb-12 lg:mb-20 tracking-tight leading-tight relative z-20">
            Não é mais um app de controle.<br>
            É um <span class="font-normal italic font-playfair text-[#367CF5]">mapa do seu futuro.</span>
        </h2>"""
content = content.replace(old_s3, new_s3)

# 7. Update Section 4
old_s4 = """        <h2 class="text-3xl md:text-4xl lg:text-5xl mb-16 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            <span class="font-normal text-white/95">Você não sai do caos para a maestria de uma noite.</span><br>
            <span class="font-bold text-white mt-2 inline-block">Você sobe uma montanha, <span class="text-[#0F172A]">passo a passo.</span></span>
        </h2>"""
new_s4 = """        <h2 class="text-3xl md:text-4xl lg:text-5xl mb-16 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            <span class="font-normal text-white/95">Você não sai do caos para a maestria de uma noite.</span><br>
            <span class="font-bold text-white mt-2 inline-block">Você sobe uma montanha, <span class="text-[#0F172A] font-normal italic font-playfair">passo a passo.</span></span>
        </h2>"""
content = content.replace(old_s4, new_s4)

# 8. Update Section 5
old_s5 = """        <h2 class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-20 text-center max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            Veja como sua vida financeira muda<br>quando você tem um mapa.
        </h2>"""
new_s5 = """        <h2 class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-20 text-center max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            Veja como sua vida financeira muda<br>quando você tem <span class="font-normal italic font-playfair text-[#A3E635]">um mapa.</span>
        </h2>"""
content = content.replace(old_s5, new_s5)

with open(filepath, 'w') as f:
    f.write(content)

