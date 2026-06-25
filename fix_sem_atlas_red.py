import re

with open('index.html', 'r') as f:
    content = f.read()

# We need to find the "Sem Atlas" div and add the red glow effect
# Current structure:
# <div class="flex-1 p-6 md:p-8 bg-black/40 border-b sm:border-b-0 sm:border-r border-white/10 flex flex-col justify-center items-center text-center">
#     <div class="flex items-center justify-center gap-2 mb-3">
#         <i data-lucide="x" class="w-4 h-4 text-rose-500 opacity-70"></i>
#         <span class="text-rose-400 font-bold text-[11px] tracking-wider uppercase">Sem Atlas</span>
#     </div>
#     <p class="text-white/60 font-medium text-lg md:text-xl leading-snug">...</p>
# </div>

def fix_sem_atlas(match):
    content_inside = match.group(1)
    # Give it bg-rose-500/10 and the same relative overflow hidden setup
    sem_bg = 'bg-rose-500/10'
    return f"""<div class="flex-1 p-6 md:p-8 {sem_bg} border-b sm:border-b-0 sm:border-r border-white/10 flex flex-col justify-center items-center text-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-rose-500/10 to-transparent pointer-events-none"></div>
                        {content_inside}
                    </div>"""

# Regex to match the Sem Atlas column
pattern = re.compile(r'<div class="flex-1 p-6 md:p-8 bg-black/40 border-b sm:border-b-0 sm:border-r border-white/10 flex flex-col justify-center items-center text-center">(.*?)</div>\s*<div class="flex-1 p-6 md:p-8 bg-\[#36DCF5\]/10', re.DOTALL)

content = pattern.sub(lambda m: fix_sem_atlas(m) + '\n                    <div class="flex-1 p-6 md:p-8 bg-[#36DCF5]/10', content)

with open('index.html', 'w') as f:
    f.write(content)
