import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Increase table container width
content = content.replace(
    '<div class="w-full max-w-5xl mx-auto">',
    '<div class="w-full max-w-6xl mx-auto">'
)

# 2. Reduce Desktop Table padding & text size
# The table body wrapper
content = content.replace(
    '<tbody class="text-sm lg:text-base">',
    '<tbody class="text-xs md:text-sm">'
)

# Replace cell paddings
content = content.replace('class="p-5 font-bold', 'class="p-3 lg:p-4 font-bold')
content = content.replace('class="p-5 text-white/60', 'class="p-3 lg:p-4 text-white/60')
content = content.replace('class="p-5 text-white/90', 'class="p-3 lg:p-4 text-white/90')

# Desktop Headers
content = content.replace(
    'py-4 font-bold text-lg rounded-t-xl',
    'py-3 font-bold text-base rounded-t-xl'
)
content = content.replace(
    'py-5 font-extrabold text-xl rounded-t-xl',
    'py-4 font-extrabold text-lg rounded-t-xl'
)

# 3. Reduce Mobile Cards padding & text size
# Cards container
content = content.replace(
    '<div class="bg-[#0B1A30] rounded-xl p-5 shadow-xl border border-white/10">',
    '<div class="bg-[#0B1A30] rounded-xl p-4 shadow-xl border border-white/10">'
)
content = content.replace(
    '<h3 class="text-white font-bold text-lg mb-4 text-center',
    '<h3 class="text-white font-bold text-base mb-3 text-center'
)
content = content.replace(
    '<div class="bg-gradient-to-r from-[#A3E635]/10 to-[#84cc16]/10 p-3 rounded-lg',
    '<div class="bg-gradient-to-r from-[#A3E635]/10 to-[#84cc16]/10 p-2.5 rounded-lg'
)

with open(filepath, 'w') as f:
    f.write(content)

