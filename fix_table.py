import re

def fix_table(content):
    # Fix the header
    content = content.replace(
        '<div class="bg-zinc-50 p-6 font-bold text-zinc-700 flex items-center">Funcionalidades</div>',
        '<div class="bg-zinc-50 p-6 font-bold text-zinc-700 flex items-center sticky left-0 z-10">Funcionalidades</div>'
    )
    
    # Fix the odd rows (which don't have a background class, so they are transparent over the table's white background)
    # They look like: <div class="p-4 px-6 text-zinc-700 font-medium">
    content = re.sub(
        r'<div class="p-4 px-6 text-zinc-700 font-medium">',
        r'<div class="p-4 px-6 text-zinc-700 font-medium bg-white sticky left-0 z-10 border-r border-zinc-200">',
        content
    )
    
    # Fix the even rows (which have bg-zinc-50/50)
    # They look like: <div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">
    # Note: bg-zinc-50/50 is transparent, so we should make it solid bg-zinc-50
    content = re.sub(
        r'<div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50/50">',
        r'<div class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50 sticky left-0 z-10 border-r border-zinc-200">',
        content
    )
    
    # And we should also make sure the table container doesn't hide the border 
    # Actually `divide-x` will handle borders between columns, but `sticky` might cause border glitches if not careful.
    # The explicit `border-r border-zinc-200` is good just in case.

    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_table(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
