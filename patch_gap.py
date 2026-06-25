import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Fix gap in s3-bottom
old_s3_bottom = 'class="w-full bg-white flex flex-col items-center pb-32 z-30 relative -mt-8 md:-mt-16 lg:-mt-24"'
new_s3_bottom = 'class="w-full bg-white flex flex-col items-center pb-12 md:pb-32 z-30 relative -mt-8 md:-mt-16 lg:-mt-24"'
content = content.replace(old_s3_bottom, new_s3_bottom)

with open(filepath, 'w') as f:
    f.write(content)

