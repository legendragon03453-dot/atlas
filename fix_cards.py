import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the classes for the left column (bg-black/20)
# Make it bg-white/5
content = content.replace('bg-black/20 flex items-center justify-center md:justify-start', 'bg-white/5 flex items-center justify-center md:justify-start')

# Function to replace the middle (Sem Atlas) and right (Com Atlas) columns
def fix_card_columns(match):
    sem_bg = 'bg-black/40' # Darker, elegant gloomy
    com_bg = 'bg-[#36DCF5]/10' # Subtle cyan/blue glow
    
    # We'll rewrite the inner HTML of the flex-1 container for the two columns
    # Group 1: Sem Atlas text
    # Group 2: Com Atlas text
    
    sem_text = match.group(1)
    com_text = match.group(2)
    
    return f"""<div class="flex-1 flex flex-col sm:flex-row">
                    <div class="flex-1 p-6 md:p-8 {sem_bg} border-b sm:border-b-0 sm:border-r border-white/10 flex flex-col justify-center items-center text-center">
                        <div class="flex items-center justify-center gap-2 mb-3">
                            <i data-lucide="x" class="w-4 h-4 text-rose-500 opacity-70"></i>
                            <span class="text-rose-400 font-bold text-[11px] tracking-wider uppercase">Sem Atlas</span>
                        </div>
                        <p class="text-white/60 font-medium text-lg md:text-xl leading-snug">{sem_text}</p>
                    </div>
                    <div class="flex-1 p-6 md:p-8 {com_bg} flex flex-col justify-center items-center text-center relative overflow-hidden">
                        <div class="absolute inset-0 bg-gradient-to-br from-[#36DCF5]/5 to-transparent pointer-events-none"></div>
                        <div class="flex items-center justify-center gap-2 mb-3 relative z-10">
                            <i data-lucide="check" class="w-4 h-4 text-[#36DCF5]"></i>
                            <span class="text-[#36DCF5] font-bold text-[11px] tracking-wider uppercase">Com Atlas</span>
                        </div>
                        <p class="text-white font-bold text-lg md:text-xl leading-snug relative z-10">{com_text}</p>
                    </div>
                </div>"""

pattern = re.compile(r'<div class="flex-1 flex flex-col sm:flex-row">.*?<span class="text-red-400 font-bold text-\[11px\] tracking-wider uppercase">Sem Atlas</span>.*?</div>\s*<p class="text-white/80 font-medium text-base md:text-lg">(.*?)</p>\s*</div>.*?<span class="text-\[#36DCF5\] font-bold text-\[11px\] tracking-wider uppercase">Com Atlas</span>.*?</div>\s*<p class="text-white font-bold text-lg md:text-xl">(.*?)</p>\s*</div>\s*</div>', re.DOTALL)

content = pattern.sub(fix_card_columns, content)

with open('index.html', 'w') as f:
    f.write(content)
