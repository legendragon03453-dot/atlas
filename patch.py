import os

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Fix header size and padding
content = content.replace(
    '<div id="s3-content" class="w-full flex flex-col items-center pt-20 md:pt-32 opacity-0 z-20 pb-16">',
    '<div id="s3-content" class="w-full flex flex-col items-center pt-8 md:pt-12 opacity-0 z-20 pb-16">'
)
content = content.replace(
    '<h2 class="text-white text-3xl md:text-5xl font-bold mb-10 text-center px-4 drop-shadow-lg">',
    '<h2 class="text-white text-2xl md:text-4xl font-bold mb-8 text-center px-4 drop-shadow-lg">'
)

# Fix BASE image negative margin
content = content.replace(
    '<div class="w-full relative -mt-40 md:-mt-64 lg:-mt-[500px] xl:-mt-[600px] z-0 pointer-events-none">',
    '<div class="w-full relative -mt-16 md:-mt-32 lg:-mt-48 xl:-mt-64 z-0 pointer-events-none">'
)

# Fix s3-bottom background color and margin
content = content.replace(
    '<section id="s3-bottom" class="w-full bg-white flex flex-col items-center pb-32 z-30 relative -mt-20 md:-mt-40 lg:-mt-56">',
    '<section id="s3-bottom" class="w-full bg-[#FEFEFE] flex flex-col items-center pb-32 z-30 relative -mt-8 md:-mt-16 lg:-mt-24">'
)

with open(filepath, 'w') as f:
    f.write(content)
