import re

def fix_s3_section(content):
    # 1. Add top padding to the wrapper to prevent the header from being cut off
    content = content.replace('id="s3-content" class="w-full flex flex-col items-center pt-8 md:pt-12 z-20', 'id="s3-content" class="w-full flex flex-col items-center pt-16 md:pt-32 z-20')
    
    # Alternatively, if we just want to push the header down
    # content = content.replace('<h2 class="text-white text-2xl md:text-4xl font-bold mb-8 text-center px-4 drop-shadow-lg ">', '<h2 class="text-white text-2xl md:text-4xl font-bold mb-8 mt-12 text-center px-4 drop-shadow-lg ">')

    # 2. Change MacBook image
    content = content.replace('https://github.com/legendragon03453-dot/atlas/blob/main/MACBOOK.webp?raw=true', 'https://github.com/legendragon03453-dot/atlas/blob/main/MAC%201.webp?raw=true')

    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_s3_section(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
