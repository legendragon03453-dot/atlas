import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Navbar Mobile Logo + Hambuguer Only
content = content.replace('class="nav-links flex-1 flex justify-center', 'class="nav-links flex-1 hidden md:flex justify-center')

# 2. Respiro azul S3-S4 (remove pb-16 from s3-content on mobile)
content = content.replace('<div id="s3-content" class="w-full flex flex-col items-center pt-8 md:pt-12 z-20 pb-16">', '<div id="s3-content" class="w-full flex flex-col items-center pt-8 md:pt-12 z-20 pb-0 md:pb-16">')
# also adjust s3-bottom margin just in case
content = content.replace('class="w-full bg-white flex flex-col items-center pb-12 md:pb-32 z-30 relative -mt-8 md:-mt-16 lg:-mt-24"', 'class="w-full bg-white flex flex-col items-center pb-12 md:pb-32 z-30 relative -mt-12 md:-mt-16 lg:-mt-24"')


# 3. S4 Title Move & Button Margin
# Extract title
title_match = re.search(r'(<!-- Título -->\s*<h2 class="text-2xl md:text-4xl lg:text-5xl mb-16 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight">.*?</h2>)', content, re.DOTALL)
if title_match:
    title_html = title_match.group(1)
    # Remove it from its current position
    content = content.replace(title_html, '')
    
    # Adjust margins in title_html
    title_html = title_html.replace('mb-16', 'mb-10 md:mb-16 mt-8 md:mt-0')
    
    # Insert it above <!-- Timeline Direta Mobile -->
    content = content.replace('<!-- Timeline Direta Mobile -->', title_html + '\n\n        <!-- Timeline Direta Mobile -->')

# Change S4 button margin
old_btn = 'gap-3 mt-24 relative z-10 w-[90%]'
new_btn = 'gap-3 mt-10 md:mt-24 relative z-10 w-[90%]'
content = content.replace(old_btn, new_btn)


# 4. Yin-Yang (S6) Mobile Divs Gap
# Find: <div class="md:hidden flex flex-col gap-6">
# Note: we need to make sure we hit the correct one in S6, but there's probably only one like this. Let's check context.
old_container = '<div class="md:hidden flex flex-col gap-6">\n\n                <div class="bg-[#0B1A30] rounded-xl p-4 shadow-xl border border-white/10">'
new_container = '<div class="md:hidden flex flex-col gap-0 border border-white/10 rounded-xl overflow-hidden shadow-xl">\n\n                <div class="bg-[#0B1A30] p-4 border-b border-white/10">'
content = content.replace(old_container, new_container)

# Replace the inner cards classes
content = content.replace('<div class="bg-[#0B1A30] rounded-xl p-4 shadow-xl border border-white/10">', '<div class="bg-[#0B1A30] p-4 border-b border-white/10">')

with open(filepath, 'w') as f:
    f.write(content)

