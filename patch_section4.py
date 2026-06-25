import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update the title HTML
old_title = """        <!-- Título -->
        <h2 class="text-white text-3xl md:text-4xl lg:text-5xl font-bold mb-16 text-center px-4 max-w-4xl leading-tight drop-shadow-lg">
            Você não sai do caos para a maestria de uma noite.<br>
            Você sobe uma montanha, passo a passo.
        </h2>"""

new_title = """        <!-- Título -->
        <h2 class="text-3xl md:text-4xl lg:text-5xl mb-16 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight">
            <span class="font-normal text-white/95">Você não sai do caos para a maestria de uma noite.</span><br>
            <span class="font-bold text-white mt-2 inline-block">Você sobe uma montanha, <span class="text-[#0F172A]">passo a passo.</span></span>
        </h2>"""

content = content.replace(old_title, new_title)

# 2. Update SVG path to end at the center (500)
old_path = "M 500 0 C 500 100, 350 100, 350 200 C 350 350, 750 350, 750 500 C 750 650, 250 650, 250 800 C 250 950, 700 950, 700 1100 C 700 1250, 450 1250, 450 1400 C 450 1500, 450 1600, 450 1600"
new_path = "M 500 0 C 500 100, 350 100, 350 200 C 350 350, 750 350, 750 500 C 750 650, 250 650, 250 800 C 250 950, 700 950, 700 1100 C 700 1250, 450 1250, 450 1400 C 450 1500, 500 1500, 500 1600"
content = content.replace(old_path, new_path)

with open(filepath, 'w') as f:
    f.write(content)

