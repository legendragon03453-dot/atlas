import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Fix Macbook size
content = content.replace(
    '<img src="https://github.com/legendragon03453-dot/atlas/blob/main/MACBOOK.webp?raw=true" alt="Macbook Dashboard" class="w-full max-w-4xl relative z-10 px-4">',
    '<img src="https://github.com/legendragon03453-dot/atlas/blob/main/MACBOOK.webp?raw=true" alt="Macbook Dashboard" class="w-full max-w-3xl relative z-10 px-4">'
)

# Fix Card 1 size (left)
old_card_1 = '<div class="lg:absolute lg:left-4 xl:left-12 top-[15%] p-6 border border-white/30 rounded-lg max-w-[320px] text-left mb-6 lg:mb-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30">'
new_card_1 = '<div class="lg:absolute lg:left-4 xl:left-12 top-[15%] p-5 border border-white/30 rounded-lg max-w-[280px] text-left mb-6 lg:mb-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30">'
content = content.replace(old_card_1, new_card_1)

# Fix Card 2 size (right)
old_card_2 = '<div class="lg:absolute lg:right-4 xl:right-12 top-[15%] p-6 border border-white/30 rounded-lg max-w-[320px] text-left mt-6 lg:mt-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30">'
new_card_2 = '<div class="lg:absolute lg:right-4 xl:right-12 top-[15%] p-5 border border-white/30 rounded-lg max-w-[280px] text-left mt-6 lg:mt-0 bg-[#367CF5]/80 backdrop-blur-md shadow-xl z-30">'
content = content.replace(old_card_2, new_card_2)

# Adjust texts in both cards to be slightly smaller to fit the smaller cards gracefully
# Both cards share this structure for title and text:
content = content.replace(
    '<h3 class="text-white text-lg font-bold mb-3 leading-tight">',
    '<h3 class="text-white text-base font-bold mb-2 leading-tight">'
)
content = content.replace(
    '<p class="text-white/90 text-sm leading-relaxed font-light">',
    '<p class="text-white/90 text-[13px] leading-relaxed font-light">'
)

with open(filepath, 'w') as f:
    f.write(content)
