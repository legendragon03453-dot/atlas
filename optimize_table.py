import re

def optimize_table_for_mobile(content):
    # Table container
    content = content.replace(
        'class="min-w-[700px] grid grid-cols-4 divide-x',
        'class="w-full min-w-full md:min-w-[700px] grid grid-cols-[1.6fr_1fr_1fr_1fr] md:grid-cols-4 divide-x'
    )
    
    # Headers
    content = content.replace(
        'class="bg-zinc-50 p-6 font-bold text-zinc-700 flex items-center sticky left-0 z-10"',
        'class="bg-zinc-50 p-2 md:p-6 font-bold text-zinc-700 flex items-center sticky left-0 z-10 text-[10px] sm:text-xs md:text-base leading-tight"'
    )
    content = content.replace(
        'class="bg-zinc-50 p-6 font-bold text-center text-atlas-dark text-lg"',
        'class="bg-zinc-50 p-2 md:p-6 font-bold text-center text-atlas-dark text-[10px] sm:text-xs md:text-lg flex items-center justify-center"'
    )
    content = content.replace(
        'class="bg-atlas-lightBlue/10 p-6 font-bold text-center text-atlas-blue text-lg border-b-2 border-atlas-blue"',
        'class="bg-atlas-lightBlue/10 p-2 md:p-6 font-bold text-center text-atlas-blue text-[10px] sm:text-xs md:text-lg border-b-2 border-atlas-blue flex items-center justify-center"'
    )
    
    # Left column cells
    content = content.replace(
        'class="p-4 px-6 text-zinc-700 font-medium bg-white sticky left-0 z-10 border-r border-zinc-200"',
        'class="p-2 md:p-4 md:px-6 text-zinc-700 font-medium bg-white sticky left-0 z-10 border-r border-zinc-200 text-[10px] sm:text-xs md:text-sm leading-tight flex items-center"'
    )
    content = content.replace(
        'class="p-4 px-6 text-zinc-700 font-medium bg-zinc-50 sticky left-0 z-10 border-r border-zinc-200"',
        'class="p-2 md:p-4 md:px-6 text-zinc-700 font-medium bg-zinc-50 sticky left-0 z-10 border-r border-zinc-200 text-[10px] sm:text-xs md:text-sm leading-tight flex items-center"'
    )
    
    # Icon cells
    content = content.replace(
        'class="p-4 flex justify-center items-center bg-zinc-50/50"',
        'class="p-2 md:p-4 flex justify-center items-center bg-zinc-50/50"'
    )
    content = content.replace(
        'class="p-4 flex justify-center items-center bg-atlas-lightBlue/10/50"',
        'class="p-2 md:p-4 flex justify-center items-center bg-atlas-lightBlue/10/50"'
    )
    content = content.replace(
        'class="p-4 flex justify-center items-center"',
        'class="p-2 md:p-4 flex justify-center items-center bg-white"'
    )
    
    # Text cells (e.g., "Comunidade", "Email")
    content = content.replace(
        'class="p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-500 font-medium"',
        'class="p-2 md:p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-500 font-medium text-[10px] md:text-sm"'
    )
    content = content.replace(
        'class="p-4 flex justify-center items-center bg-atlas-lightBlue/10/50 text-zinc-700 font-medium"',
        'class="p-2 md:p-4 flex justify-center items-center bg-atlas-lightBlue/10/50 text-zinc-700 font-medium text-[10px] md:text-sm"'
    )
    content = content.replace(
        'class="p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-700 font-medium"',
        'class="p-2 md:p-4 flex justify-center items-center bg-zinc-50/50 text-zinc-700 font-medium text-[10px] md:text-sm"'
    )
    
    # Icons size
    content = content.replace('class="w-5 h-5 text-atlas-blue"', 'class="w-4 h-4 md:w-5 md:h-5 text-atlas-blue"')
    content = content.replace('class="w-5 h-5 text-zinc-300"', 'class="w-4 h-4 md:w-5 md:h-5 text-zinc-300"')
    
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = optimize_table_for_mobile(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
