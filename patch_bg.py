import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Section 3
content = content.replace(
    '<section id="s3-bottom" class="w-full bg-[#FEFEFE]',
    '<section id="s3-bottom" class="w-full bg-white'
)

# Section 6
content = content.replace(
    '<section id="section-6" class="w-full bg-zinc-50',
    '<section id="section-6" class="w-full bg-white'
)

# Section 8
content = content.replace(
    '<section id="section-8" class="w-full bg-gradient-to-b from-white to-[#f4f7fe]',
    '<section id="section-8" class="w-full bg-white'
)

with open(filepath, 'w') as f:
    f.write(content)

