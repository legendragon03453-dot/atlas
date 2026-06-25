import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update Grid Max-Width
content = content.replace(
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 max-w-5xl mx-auto mb-20 relative z-10">',
    '<div class="grid grid-cols-1 md:grid-cols-3 gap-6 lg:gap-8 max-w-6xl mx-auto mb-20 relative z-10">'
)

# 2. Update Gap (mt-8 -> mt-12)
content = content.replace('<ul class="mt-8 space-y-4">', '<ul class="mt-14 space-y-4">')

# 3. Animate middle button & add animation CSS
style_end = content.find('</style>')
heartbeat_css = """
        @keyframes heartbeat {
            0%, 100% { transform: scale(1); }
            50% { transform: scale(1.05); }
        }
        .animate-heartbeat {
            animation: heartbeat 2s ease-in-out infinite;
        }
"""
if 'keyframes heartbeat' not in content:
    content = content[:style_end] + heartbeat_css + content[style_end:]

old_pro_btn = '<button class="w-full py-4 rounded-xl bg-[#A3E635] text-[#0B1A30] font-extrabold hover:bg-[#8cdc18] transition-all shadow-[0_4px_14px_0_rgba(163,230,53,0.39)]">Assinar Plano</button>'
new_pro_btn = '<button class="w-full py-4 rounded-xl bg-[#A3E635] text-[#0B1A30] font-extrabold hover:bg-[#8cdc18] transition-all shadow-[0_4px_14px_0_rgba(163,230,53,0.39)] animate-heartbeat">Assinar Plano</button>'
content = content.replace(old_pro_btn, new_pro_btn)

# 4. Add IDs to toggle buttons
old_toggle = """                <!-- Toggle Mensal/Anual -->
                <div class="flex items-center mt-4 bg-white border border-blue-100 p-1.5 rounded-full shadow-sm">
                    <button class="px-6 py-2 rounded-full bg-[#367CF5] text-white font-semibold text-sm transition-all shadow-md">Mensal</button>
                    <button class="px-6 py-2 rounded-full text-zinc-500 font-semibold text-sm hover:text-zinc-800 transition-all">Anual</button>
                </div>"""
new_toggle = """                <!-- Toggle Mensal/Anual -->
                <div class="flex items-center mt-4 bg-white border border-blue-100 p-1.5 rounded-full shadow-sm">
                    <button id="btn-mensal" class="px-6 py-2 rounded-full bg-[#367CF5] text-white font-semibold text-sm transition-all shadow-md">Mensal</button>
                    <button id="btn-anual" class="px-6 py-2 rounded-full text-zinc-500 font-semibold text-sm hover:text-zinc-800 transition-all">Anual</button>
                </div>"""
content = content.replace(old_toggle, new_toggle)

# 5. Add data attributes to prices
# Essencial
old_price_1 = """                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 15,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>"""
new_price_1 = """                            <span class="text-4xl font-bold text-[#1a1a1a] price-value" data-mensal="15,90" data-anual="190,80">R$ 15,90</span>
                            <span class="text-zinc-500 font-medium mb-1 price-period">/mês</span>"""
content = content.replace(old_price_1, new_price_1)

# Pro
old_price_2 = """                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 24,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>"""
new_price_2 = """                            <span class="text-4xl font-bold text-[#1a1a1a] price-value" data-mensal="24,90" data-anual="298,80">R$ 24,90</span>
                            <span class="text-zinc-500 font-medium mb-1 price-period">/mês</span>"""
content = content.replace(old_price_2, new_price_2)

# Elite
old_price_3 = """                            <span class="text-4xl font-bold text-[#1a1a1a]">R$ 32,90</span>
                            <span class="text-zinc-500 font-medium mb-1">/mês</span>"""
new_price_3 = """                            <span class="text-4xl font-bold text-[#1a1a1a] price-value" data-mensal="32,90" data-anual="394,80">R$ 32,90</span>
                            <span class="text-zinc-500 font-medium mb-1 price-period">/mês</span>"""
content = content.replace(old_price_3, new_price_3)

# 6. Add JS script for toggle
script_end = content.find('</script>')
js_toggle = """
        // Mensal / Anual Toggle
        const btnMensal = document.getElementById('btn-mensal');
        const btnAnual = document.getElementById('btn-anual');
        const priceValues = document.querySelectorAll('.price-value');
        const pricePeriods = document.querySelectorAll('.price-period');

        if(btnMensal && btnAnual) {
            btnMensal.addEventListener('click', () => {
                btnMensal.classList.add('bg-[#367CF5]', 'text-white', 'shadow-md');
                btnMensal.classList.remove('text-zinc-500');
                btnAnual.classList.remove('bg-[#367CF5]', 'text-white', 'shadow-md');
                btnAnual.classList.add('text-zinc-500');
                
                priceValues.forEach(el => el.textContent = 'R$ ' + el.getAttribute('data-mensal'));
                pricePeriods.forEach(el => el.textContent = '/mês');
            });

            btnAnual.addEventListener('click', () => {
                btnAnual.classList.add('bg-[#367CF5]', 'text-white', 'shadow-md');
                btnAnual.classList.remove('text-zinc-500');
                btnMensal.classList.remove('bg-[#367CF5]', 'text-white', 'shadow-md');
                btnMensal.classList.add('text-zinc-500');
                
                priceValues.forEach(el => el.textContent = 'R$ ' + el.getAttribute('data-anual'));
                pricePeriods.forEach(el => el.textContent = '/ano');
            });
        }
"""
if '// Mensal / Anual Toggle' not in content:
    content = content[:script_end] + js_toggle + content[script_end:]

with open(filepath, 'w') as f:
    f.write(content)

