import re

with open('index.html', 'r') as f:
    content = f.read()

# Add scroll-reveal class to headings, paragraphs, and cards in sections 4 onwards
# We can just add it to a few specific classes to be safe.
# Find elements like `class="card ` or `class="bg-white rounded-2xl`
content = re.sub(r'class="([^"]*rounded-[x2]l[^"]*bg-white[^"]*)"', r'class="\1 scroll-reveal"', content)
content = re.sub(r'class="([^"]*text-3xl[^"]*font-bold[^"]*)"', r'class="\1 scroll-reveal"', content)
content = re.sub(r'class="([^"]*text-4xl[^"]*font-bold[^"]*)"', r'class="\1 scroll-reveal"', content)
content = re.sub(r'class="([^"]*text-5xl[^"]*font-bold[^"]*)"', r'class="\1 scroll-reveal"', content)

with open('index.html', 'w') as f:
    f.write(content)

