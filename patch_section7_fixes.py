import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Background branca
content = content.replace(
    '<section id="section-7" class="w-full bg-[#F9F6F0] py-24 md:py-40 px-6 lg:px-12 text-[#1a1a1a] relative border-t border-[#e2dfd8]">',
    '<section id="section-7" class="w-full bg-white py-24 md:py-40 px-6 lg:px-12 text-[#1a1a1a] relative border-t border-zinc-200">'
)

# 2. Imagem no lugar do abstrato
old_visual = """                    <!-- Visual Conceitual/Abstrato -->
                    <div class="w-full h-64 bg-gradient-to-br from-[#e2dfd8] to-[#d4d0c8] rounded-2xl relative overflow-hidden hidden lg:block shadow-inner">
                        <div class="absolute inset-0 bg-[radial-gradient(circle_at_top_right,rgba(255,255,255,0.4)_0%,transparent_60%)]"></div>
                        <div class="absolute bottom-[-20%] left-[-10%] w-[120%] h-[120%] bg-[radial-gradient(circle_at_bottom_left,rgba(54,124,245,0.05)_0%,transparent_60%)]"></div>
                    </div>"""
new_visual = """                    <!-- Imagem Fornecida -->
                    <div class="w-full h-64 rounded-2xl relative overflow-hidden hidden lg:block shadow-md">
                        <img src="https://github.com/legendragon03453-dot/atlas/blob/main/Imagem%20de%20Fundo%204%20relatorios%202.png?raw=true" alt="Imagem 4 relatórios" class="w-full h-full object-cover object-center">
                    </div>"""
content = content.replace(old_visual, new_visual)

# 3. Remover Drop Cap (letra C)
old_p1 = """                <p>
                    <span class="float-left text-7xl lg:text-8xl font-playfair font-normal italic text-[#367CF5] leading-[0.8] pr-3 pt-2">C</span>
                    resci em uma pousada no litoral de Santa Catarina. Meus pais tiveram o negócio por 25 anos sem planejamento. Em 2020, fechou.
                </p>"""
new_p1 = """                <p>
                    Cresci em uma pousada no litoral de Santa Catarina. Meus pais tiveram o negócio por 25 anos sem planejamento. Em 2020, fechou.
                </p>"""
content = content.replace(old_p1, new_p1)

# 4. Mudar verde para azul
old_highlight = '<span class="bg-[#A3E635]/30 px-2 py-0.5 rounded">Era falta de mapa.</span>'
new_highlight = '<span class="bg-[#367CF5]/20 text-[#367CF5] font-bold px-2 py-0.5 rounded">Era falta de mapa.</span>'
content = content.replace(old_highlight, new_highlight)

old_strong = '<strong class="font-playfair italic font-normal text-3xl md:text-4xl text-[#A3E635]">É o mapa que meus pais não tiveram quando precisaram.</strong>'
new_strong = '<strong class="font-playfair italic font-normal text-3xl md:text-4xl text-[#36DCF5]">É o mapa que meus pais não tiveram quando precisaram.</strong>'
content = content.replace(old_strong, new_strong)


with open(filepath, 'w') as f:
    f.write(content)
