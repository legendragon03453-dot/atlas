import re

def solidify_cards(content):
    # 1. Main card container
    # old: bg-white md:bg-white/10 backdrop-blur-md border-gray-200 md:border-white/20
    # new: bg-white border-gray-200 shadow-md
    content = content.replace('bg-white md:bg-white/10 backdrop-blur-md border-gray-200 md:border-white/20', 'bg-white border-gray-200 shadow-lg')
    content = content.replace('bg-white md:bg-white/10 border border-zinc-200 md:border-white/20 rounded-2xl px-5 py-4 flex-1 backdrop-blur-sm shadow-md md:shadow-none', 'bg-white border border-gray-200 rounded-2xl px-5 py-4 flex-1 shadow-md')
    content = content.replace('bg-white md:bg-white/10 backdrop-blur-sm border border-zinc-200 md:border-white/20 p-3 rounded-lg flex items-center justify-center text-center shadow-lg', 'bg-white border border-gray-200 p-3 rounded-lg flex items-center justify-center text-center shadow-md')

    # 2. Card left side (title part)
    # old: bg-transparent md:bg-white/5
    # new: bg-white
    content = content.replace('bg-transparent md:bg-white/5', 'bg-white')

    # 3. Card right side (content part)
    # old: bg-atlas-lightBlue/10 md:bg-white/20
    # new: bg-white
    content = content.replace('bg-atlas-lightBlue/10 md:bg-white/20', 'bg-white')
    content = content.replace('border-gray-100 md:border-white/5', 'border-gray-100')

    # 4. Remove any rogue md:bg-white/something that might be left
    content = re.sub(r'\bmd:bg-white/[0-9]+\b', '', content)
    
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = solidify_cards(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
