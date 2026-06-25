import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Fix Section 4 wrapper
old_sec4 = 'class="w-full bg-[#367CF5] flex flex-col items-center pt-2 md:pt-24 pb-20 md:pb-32 relative overflow-hidden -mt-10 lg:mt-0"'
new_sec4 = 'class="w-full bg-[#367CF5] flex flex-col items-center pt-16 md:pt-24 pb-20 md:pb-32 relative overflow-hidden lg:mt-0"'
content = content.replace(old_sec4, new_sec4)

# 2. Fix Header margin
old_h2 = 'class="text-2xl md:text-4xl lg:text-5xl mb-10 md:mb-16 mt-[50px] md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight"'
new_h2 = 'class="text-2xl md:text-4xl lg:text-5xl mb-4 md:mb-16 mt-20 md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight"'
content = content.replace(old_h2, new_h2)

# 3. Fix Mobile Cards Container margin
old_cards = 'class="md:hidden flex flex-col gap-6 w-[90%] mx-auto mt-8 relative z-20"'
new_cards = 'class="md:hidden flex flex-col gap-6 w-[90%] mx-auto mt-2 relative z-20"'
content = content.replace(old_cards, new_cards)

with open('index.html', 'w') as f:
    f.write(content)

