import re

with open('funcionalidades.html', 'r') as f:
    content = f.read()

def insert_image(heading, img_url):
    global content
    img_tag = f'<div class="mt-6 rounded-xl overflow-hidden border border-zinc-200 shadow-sm"><img src="{img_url}" alt="Screenshot" class="w-full h-auto"></div>'
    # Look for the heading, then the paragraph following it, and insert the image after the paragraph.
    # Pattern: </h3> followed by <p ...>...</p> or <ul ...>...</ul>
    pattern = r'(<h3 class="[^"]*">' + re.escape(heading) + r'</h3>\s*<p class="[^"]*">.*?</p>)'
    if re.search(pattern, content, flags=re.DOTALL):
        content = re.sub(pattern, r'\1\n' + img_tag, content, count=1, flags=re.DOTALL)
    else:
        # If no paragraph, insert directly after heading
        pattern = r'(<h3 class="[^"]*">' + re.escape(heading) + r'</h3>)'
        content = re.sub(pattern, r'\1\n' + img_tag, content, count=1, flags=re.DOTALL)

# Insert specific images below their block headings
img1 = "https://github.com/legendragon03453-dot/atlas/raw/main/ATLAS/IMG%201_1x.webp"
img2 = "https://github.com/legendragon03453-dot/atlas/raw/main/ATLAS/IMG%202_1x.webp"
img3 = "https://github.com/legendragon03453-dot/atlas/raw/main/ATLAS/IMG%203_1x.webp"
img7 = "https://github.com/legendragon03453-dot/atlas/raw/main/ATLAS/IMG%207_1x.webp"
img6 = "https://github.com/legendragon03453-dot/atlas/raw/main/ATLAS/IMG%206_1x.webp"

insert_image("Lançamento Diário Organizado (8 Abas)", img1) # Dia a dia
insert_image("Simulador de Decisão", img2) # Decisões
insert_image("Aposentadoria: 3 Respostas Diferentes", img3)
insert_image("Objetivos de Vida Mapeados", img7)
insert_image("Calendário de Pagamentos", img6)

# Remove PRO from Calculadoras Express
content = content.replace('<div class="absolute top-4 right-4 bg-[#367CF5] text-white text-[10px] font-bold px-2 py-1 rounded">PRO</div>\n                        <h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Calculadoras Express</h3>', '<h3 class="text-lg font-bold text-[#1a1a1a] mb-2">Calculadoras Express</h3>')

# Add 5 images to Método Atlas
for i in range(1, 6):
    img_tag = f'<div class="mt-4 rounded-lg overflow-hidden border border-zinc-200"><img src="https://via.placeholder.com/600x300?text=Etapa+{i}+-+Em+breve" alt="Etapa {i}" class="w-full h-auto"></div>'
    if i == 1: heading = "1. A Vista da Montanha"
    elif i == 2: heading = "2. Base da Montanha"
    elif i == 3: heading = "3. Estratégia de Subida"
    elif i == 4: heading = "4. Controle da Jornada"
    elif i == 5: heading = "5. Guia da Jornada"
    
    pattern = r'(<h3 class="[^"]*">' + re.escape(heading) + r'</h3>\s*<p class="[^"]*">.*?</p>)'
    content = re.sub(pattern, r'\1\n' + img_tag, content, count=1, flags=re.DOTALL)

# Update Ecossistema de Educação
old_edu = """            <!-- Ecossistema de Educação -->
            <section class="feature-section" id="educacao" class="scroll-mt-32">
                <div class="mb-8">
                    <h2 class="text-3xl font-bold text-[#0F172A] mb-2">Ecossistema de Educação</h2>
                    <p class="text-zinc-500 text-lg">Aprender a usar o app é a metade. Aprender a pensar diferente é a outra metade.</p>
                </div>"""

new_edu = """            <!-- Ecossistema de Educação -->
            <section class="feature-section" id="educacao" class="scroll-mt-32">
                <div class="mb-8 flex items-center gap-3">
                    <h2 class="text-3xl font-bold text-[#0F172A]">Ecossistema de Educação</h2>
                    <span class="bg-amber-400 text-[#1A2E05] text-xs font-bold px-2.5 py-1 rounded-md uppercase tracking-wider">Em breve</span>
                </div>
                <p class="text-zinc-500 text-lg mb-8">Aprender a usar o app é a metade. Aprender a pensar diferente é a outra metade. Nossos treinamentos completos estarão integrados aqui.</p>
                
                <div class="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
                    <div class="bg-zinc-100 p-6 rounded-2xl border border-zinc-200 text-center opacity-70">
                        <h3 class="font-bold text-zinc-700">O Plano da Liberdade</h3>
                    </div>
                    <div class="bg-zinc-100 p-6 rounded-2xl border border-zinc-200 text-center opacity-70">
                        <h3 class="font-bold text-zinc-700">Manual do Dinheiro</h3>
                    </div>
                    <div class="bg-zinc-100 p-6 rounded-2xl border border-zinc-200 text-center opacity-70">
                        <h3 class="font-bold text-zinc-700">Atlas Negócios (Curso)</h3>
                    </div>
                </div>"""

# Find the start of old_edu and replace just the intro part
if old_edu in content:
    content = content.replace(old_edu, new_edu)

with open('funcionalidades.html', 'w') as f:
    f.write(content)

