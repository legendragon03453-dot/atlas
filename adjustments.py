import re

def adjust_site(content):
    # 1. Hero Button Size
    content = content.replace('md:px-20 md:py-6 rounded-full font-black text-xl md:text-4xl', 'md:px-24 md:py-7 rounded-full font-black text-2xl md:text-5xl')
    
    # 2. Timeline subtitle color
    # old: <span class="text-atlas-dark font-normal italic font-playfair">passo a passo.</span>
    # new: <span class="text-white font-normal italic font-playfair">passo a passo.</span>
    content = content.replace('text-atlas-dark font-normal italic font-playfair">passo a passo.', 'text-white font-normal italic font-playfair">passo a passo.')
    
    # 3. Head section text color
    # old: <strong class="font-playfair italic font-normal text-2xl md:text-4xl text-atlas-blue">É o mapa que meus pais não tiveram quando precisaram.</strong>
    # new: remove text-atlas-blue to let it be white
    content = content.replace('text-2xl md:text-4xl text-atlas-blue">É o mapa que', 'text-2xl md:text-4xl text-white">É o mapa que')
    
    # 4. Pro Card looping animation
    # old: ... transform md:-translate-y-4 [animation:pulse_4s_ease-in-out_infinite]
    # new: ... transform md:-translate-y-4
    content = content.replace(' [animation:pulse_4s_ease-in-out_infinite]', '')

    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = adjust_site(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
