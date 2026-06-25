import re

with open('index.html', 'r') as f:
    content = f.read()

old_heading = """        <!-- Título -->
        <h2 class="text-2xl md:text-4xl lg:text-5xl mb-4 md:mb-16 mt-20 md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight scroll-reveal">
            <span class="font-normal text-white/95">Você não sai do caos para a maestria de uma noite.</span><br>
            <span class="font-bold text-white mt-2 inline-block">Você sobe uma montanha, <span class="text-[#0F172A] font-normal italic font-playfair">passo a passo.</span></span>
        </h2>"""

new_heading = """        <!-- Título -->
        <h2 class="text-2xl md:text-4xl lg:text-5xl mb-4 md:mb-16 mt-20 md:mt-0 text-left md:text-center px-4 md:px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight scroll-reveal border-l-4 border-[#AFFF00] md:border-l-0 ml-4 md:ml-0 pl-4 md:pl-0">
            <span class="font-normal text-white/95 block mb-2">Você não sai do caos para a maestria de uma noite.</span>
            <span class="font-bold text-white block">Você sobe uma montanha, <span class="text-[#AFFF00] md:text-[#0F172A] font-normal italic font-playfair">passo a passo.</span></span>
        </h2>"""

content = content.replace(old_heading, new_heading)

with open('index.html', 'w') as f:
    f.write(content)

