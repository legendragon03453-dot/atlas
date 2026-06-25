import os
import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update SVG path
old_path = "M 350 0 C 350 100, 350 100, 350 200 C 350 350, 750 350, 750 500 C 750 650, 250 650, 250 800 C 250 950, 700 950, 700 1100 C 700 1250, 450 1250, 450 1400 C 450 1500, 450 1600, 450 1600"
new_path = "M 500 0 C 500 100, 350 100, 350 200 C 350 350, 750 350, 750 500 C 750 650, 250 650, 250 800 C 250 950, 700 950, 700 1100 C 700 1250, 450 1250, 450 1400 C 450 1500, 450 1600, 450 1600"
content = content.replace(old_path, new_path)

# 2. Update text alignment classes inside Section 4.
# Let's locate Section 4 and replace text-right with text-left inside it.
s4_start = content.find('<!-- === SEÇÃO 4: Timeline === -->')
s4_end = content.find('<!-- === SEÇÃO 3 BOTTOM (Área Branca inferior) === -->', s4_start)

if s4_start != -1:
    # If s4_end is not found, just replace in the rest of the file
    s4_content = content[s4_start:s4_end if s4_end != -1 else len(content)]
    
    # We want to change 'md:text-right' and 'text-right' to 'text-left'
    s4_content = s4_content.replace('text-right', 'text-left')
    # Since there might be 'text-left md:text-left', let's deduplicate classes just in case,
    # but having it twice in a class attribute doesn't break anything.
    s4_content = s4_content.replace('md:text-right', 'md:text-left')
    
    content = content[:s4_start] + s4_content + (content[s4_end:] if s4_end != -1 else "")

with open(filepath, 'w') as f:
    f.write(content)

