import re

with open('index.html', 'r') as f:
    content = f.read()

# We only want to target the button in the hero section.
# The hero button is around line 424 and has:
# class="btn-green text-[#1A2E05] px-10 py-4 md:px-14 md:py-5 rounded-full font-bold text-xl md:text-2xl flex items-center justify-center gap-3 w-full sm:w-auto"

old_classes = 'btn-green text-[#1A2E05] px-10 py-4 md:px-14 md:py-5 rounded-full font-bold text-xl md:text-2xl flex items-center justify-center gap-3 w-full sm:w-auto'
new_classes = 'btn-green text-[#1A2E05] px-12 py-5 md:px-20 md:py-6 rounded-full font-bold text-2xl md:text-3xl flex items-center justify-center gap-4 w-full sm:w-auto'

# Replace only the first occurrence (which is the hero button)
content = content.replace(old_classes, new_classes, 1)

with open('index.html', 'w') as f:
    f.write(content)

