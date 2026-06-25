import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update margin for heading
old_heading = 'class="text-2xl md:text-4xl lg:text-5xl mb-10 md:mb-16 mt-8 md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight scroll-reveal"'
new_heading = 'class="text-2xl md:text-4xl lg:text-5xl mb-10 md:mb-16 mt-[50px] md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight scroll-reveal"'

if old_heading not in content:
    old_heading = 'class="text-2xl md:text-4xl lg:text-5xl mb-10 md:mb-16 mt-8 md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight"'
    new_heading = 'class="text-2xl md:text-4xl lg:text-5xl mb-10 md:mb-16 mt-[50px] md:mt-0 text-center px-4 max-w-4xl leading-tight drop-shadow-lg tracking-tight"'

content = content.replace(old_heading, new_heading)


# 2. Increase mobile button sizes
# Hero
old_hero = 'px-16 py-6 md:px-28 md:py-8 rounded-full font-black text-3xl md:text-4xl'
new_hero = 'py-8 md:px-28 md:py-8 rounded-full font-black text-4xl md:text-5xl'
content = content.replace(old_hero, new_hero)

# Other buttons
old_other = 'px-14 py-5 md:px-24 md:py-7 rounded-full font-bold text-2xl md:text-3xl'
new_other = 'py-6 md:px-24 md:py-7 rounded-full font-bold text-3xl md:text-4xl'
content = content.replace(old_other, new_other)

with open('index.html', 'w') as f:
    f.write(content)

