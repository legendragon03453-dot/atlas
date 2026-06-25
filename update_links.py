import re
import glob

# 1. Update all general login links
for filename in glob.glob('*.html'):
    if filename == 'current_live.html': continue
    with open(filename, 'r') as f:
        content = f.read()
    content = content.replace('https://app.atlas.com.br', 'https://app.useatlasapp.com/auth')
    with open(filename, 'w') as f:
        f.write(content)

# 2. Update specific links in index.html
with open('index.html', 'r') as f:
    index_content = f.read()

# Teste por 7 dias
# Find <a href="#section-8" class="...">\s*Teste por 7 dias\s*</a>
# Replace href with https://app.useatlasapp.com/comece
def replace_teste(match):
    return match.group(0).replace('href="#section-8"', 'href="https://app.useatlasapp.com/comece"')
index_content = re.sub(r'<a href="#section-8"[^>]*>\s*Teste por 7 dias\s*</a>', replace_teste, index_content)

# Pricing buttons
# Essencial
essencial_btn = r'<button class="w-full py-4 rounded-xl bg-\[#0B1A30\] text-white font-bold hover:bg-\[#1a2e4f\] transition-all shadow-\[0_4px_14px_0_rgba\(11,26,48,0\.39\)\]">Assinar Plano</button>'
essencial_link = '<a href="https://app.useatlasapp.com/comprar/essencial" class="block text-center w-full py-4 rounded-xl bg-[#0B1A30] text-white font-bold hover:bg-[#1a2e4f] transition-all shadow-[0_4px_14px_0_rgba(11,26,48,0.39)]">Assinar Plano</a>'

# Pro
pro_btn = r'<button class="w-full py-4 rounded-xl bg-\[#A3E635\] text-\[#0B1A30\] font-extrabold hover:bg-\[#8cdc18\] transition-all shadow-\[0_4px_14px_0_rgba\(163,230,53,0\.39\)\] animate-heartbeat">Assinar Plano</button>'
pro_link = '<a href="https://app.useatlasapp.com/comprar/pro" class="block text-center w-full py-4 rounded-xl bg-[#A3E635] text-[#0B1A30] font-extrabold hover:bg-[#8cdc18] transition-all shadow-[0_4px_14px_0_rgba(163,230,53,0.39)] animate-heartbeat">Assinar Plano</a>'

# Elite
elite_btn = r'<button class="w-full py-4 rounded-xl bg-\[#0B1A30\] text-white font-bold hover:bg-\[#1a2e4f\] transition-all shadow-\[0_4px_14px_0_rgba\(11,26,48,0\.39\)\]">Assinar Plano</button>'
elite_link = '<a href="https://app.useatlasapp.com/comprar/elite" class="block text-center w-full py-4 rounded-xl bg-[#0B1A30] text-white font-bold hover:bg-[#1a2e4f] transition-all shadow-[0_4px_14px_0_rgba(11,26,48,0.39)]">Assinar Plano</a>'

# Because Essencial and Elite have the exact same HTML, we can replace them sequentially
# 1st match -> Essencial
# 2nd match -> Elite
parts = re.split(essencial_btn, index_content)
if len(parts) == 3:
    index_content = parts[0] + essencial_link + parts[1] + elite_link + parts[2]
else:
    print("Error: Could not split Essencial/Elite buttons correctly. Found:", len(parts)-1)

index_content = re.sub(pro_btn, pro_link, index_content)

with open('index.html', 'w') as f:
    f.write(index_content)
