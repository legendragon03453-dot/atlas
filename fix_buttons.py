import re

with open('index.html', 'r') as f:
    content = f.read()

# We want to standardize the padding and text size.
# Replace occurrences of px-8 py-3, px-10 py-4, px-12 py-4, text-xl, md:text-xl
# with a standard set: px-10 py-4 md:px-12 md:py-5 text-xl md:text-2xl

# Find the hero button
content = re.sub(
    r'px-8 py-3 md:px-10 md:py-4 rounded-full font-bold text-xl',
    r'px-10 py-4 md:px-14 md:py-5 rounded-full font-bold text-xl md:text-2xl',
    content
)

# Find the other buttons
content = re.sub(
    r'px-12 py-4 rounded-full font-bold text-xl',
    r'px-10 py-4 md:px-14 md:py-5 rounded-full font-bold text-xl md:text-2xl',
    content
)

with open('index.html', 'w') as f:
    f.write(content)

