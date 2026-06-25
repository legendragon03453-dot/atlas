import re

with open('funcionalidades.html', 'r') as f:
    content = f.read()

# 1. Controle do Dia a Dia -> IMG 1
img1 = '<div class="mt-8 rounded-xl overflow-hidden border border-zinc-200 shadow-sm"><img src="https://github.com/legendragon03453-dot/atlas/raw/main/ATLAS/IMG%201_1x.webp" alt="Controle do Dia a Dia" class="w-full h-auto"></div>'
content = content.replace('<!-- Pode inserir print de tela aqui -->', img1, 1) # Only first one or find exact place

# Let's do replacements by exact heading matches:
content = re.sub(r'(<h2 class="text-2xl md:text-3xl font-bold text-\[\#1a1a1a\] mb-6">Controle do Dia a Dia</h2>.*?)(</div>)', r'\1' + img1 + r'\2', content, count=1, flags=re.DOTALL)

with open('funcionalidades.html', 'w') as f:
    f.write(content)

