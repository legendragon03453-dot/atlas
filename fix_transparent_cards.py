import re

for filename in ['index.html', 'funcionalidades.html']:
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # 1. Timeline items (Section 4 mobile)
        # Find: bg-white/10 border border-white/20 rounded-2xl px-5 py-4 flex-1 backdrop-blur-sm
        # Replace: bg-white md:bg-white/10 border border-zinc-200 md:border-white/20 rounded-2xl px-5 py-4 flex-1 backdrop-blur-sm shadow-md md:shadow-none
        old_timeline_card = 'bg-white/10 border border-white/20 rounded-2xl px-5 py-4 flex-1 backdrop-blur-sm'
        new_timeline_card = 'bg-white md:bg-white/10 border border-zinc-200 md:border-white/20 rounded-2xl px-5 py-4 flex-1 backdrop-blur-sm shadow-md md:shadow-none'
        content = content.replace(old_timeline_card, new_timeline_card)

        # Fix the paragraph inside timeline items: text-white/75 -> text-gray-600 md:text-white/75
        content = content.replace('<p class="text-white/75 text-sm', '<p class="text-gray-600 md:text-white/75 text-sm')

        # 2. Category chips (Section 2 mobile)
        # Find: bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg
        # Replace: bg-white md:bg-white/10 backdrop-blur-sm border border-zinc-200 md:border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg
        old_chip = 'bg-white/10 backdrop-blur-sm border border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg'
        new_chip = 'bg-white md:bg-white/10 backdrop-blur-sm border border-zinc-200 md:border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg'
        content = content.replace(old_chip, new_chip)

        # Fix the text inside category chips:
        # Note: the text in those chips is <span class="text-white font-bold text-sm tracking-wide">
        # BUT there are other places with "text-white font-bold text-sm tracking-wide". We only want the ones in the chips.
        # We can just use a regex for the exact ones:
        categories = ['Despesas', 'Receitas', 'Investimentos', 'Imóveis', 'Criptomoedas', 'Financiamentos']
        for cat in categories:
            old_span = f'<span class="text-white font-bold text-sm tracking-wide">{cat}</span>'
            new_span = f'<span class="text-[#367CF5] md:text-white font-bold text-sm tracking-wide">{cat}</span>'
            content = content.replace(old_span, new_span)
            
        # Also fix the text in the "Tem medo de investir errado" card which has <p class="text-white/90 text-xs font-medium leading-tight">
        content = content.replace('<p class="text-white/90 text-xs font-medium leading-tight">', '<p class="text-[#367CF5] md:text-white/90 text-xs font-medium leading-tight">')

        with open(filename, 'w') as f:
            f.write(content)
            
    except FileNotFoundError:
        pass
