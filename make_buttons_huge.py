import re

with open('index.html', 'r') as f:
    content = f.read()

# Make hero button MASSIVE
old_hero = r'px-12 py-5 md:px-20 md:py-6 rounded-full font-bold text-2xl md:text-3xl flex items-center justify-center gap-4 w-full sm:w-auto'
new_hero = r'px-16 py-6 md:px-28 md:py-8 rounded-full font-black text-3xl md:text-4xl flex items-center justify-center gap-5 w-full sm:w-[80%] md:w-auto uppercase tracking-wide'

content = content.replace(old_hero, new_hero, 1)

# Make other buttons HUGE
old_other = r'px-10 py-4 md:px-14 md:py-5 rounded-full font-bold text-xl md:text-2xl flex items-center'
new_other = r'px-14 py-5 md:px-24 md:py-7 rounded-full font-bold text-2xl md:text-3xl flex items-center'

content = content.replace(old_other, new_other)

with open('index.html', 'w') as f:
    f.write(content)

