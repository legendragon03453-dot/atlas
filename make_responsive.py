import os
import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Faster transition (scroll distance)
content = content.replace('end: "+=3000",', 'end: "+=1200",')
content = content.replace('tl.to({}, {duration: 1.5})', 'tl.to({}, {duration: 0.5})')

# 2. Section 1 Responsiveness (Title size on mobile)
content = content.replace('text-5xl md:text-6xl', 'text-4xl sm:text-5xl md:text-6xl')
content = content.replace('px-10 py-4', 'px-8 py-3 md:px-10 md:py-4') # Button size on mobile

# 3. Section 2 Responsiveness (Circle size)
# Old circle css:
# .circle-container { width: 280px; height: 280px; ... }
old_circle = """        .circle-container {
            position: relative;
            width: 280px;
            height: 280px;"""
new_circle = """        .circle-container {
            position: relative;
            width: 220px;
            height: 220px;"""
content = content.replace(old_circle, new_circle)

# Adjust snowball start size to match the new mobile circle size
content = content.replace(
    '<div id="snowball" class="absolute top-[50vh] left-[50%] w-[280px] h-[280px] md:w-[450px]',
    '<div id="snowball" class="absolute top-[50vh] left-[50%] w-[220px] h-[220px] sm:w-[280px] sm:h-[280px] md:w-[450px]'
)

# Text sizes around the circle for mobile: reduce width of text wrapper and font-size
# We can do this by regexing the absolute divs inside circle-dot
# Find all occurrences of `w-28 md:w-48 text-right` etc and make them smaller
content = content.replace('w-28 md:w-48', 'w-24 sm:w-28 md:w-48')
content = content.replace('w-32 md:w-56', 'w-24 sm:w-32 md:w-56')
content = content.replace('text-[12px] md:text-sm', 'text-[10px] sm:text-[12px] md:text-sm')

# 4. Section 3 Responsiveness
# Cards on mobile should take more width and stack nicely
content = content.replace('max-w-[280px] text-left mb-6', 'w-[90%] max-w-[320px] lg:max-w-[280px] text-left mb-6')
content = content.replace('max-w-[280px] text-left mt-6', 'w-[90%] max-w-[320px] lg:max-w-[280px] text-left mt-6')

# Base image margin on mobile
content = content.replace('-mt-16 md:-mt-32', '-mt-8 sm:-mt-16 md:-mt-32')

with open(filepath, 'w') as f:
    f.write(content)
