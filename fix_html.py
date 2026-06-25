import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Extract Section 9 and 10
s9_start = content.find('<!-- === SEÇÃO 9: FAQ === -->')
s10_end = content.find('</section>', content.find('<!-- === SEÇÃO 10: CTA FINAL === -->')) + len('</section>')

if s9_start != -1 and s10_end != -1:
    sections_9_10 = content[s9_start:s10_end]
    # Remove them from their current position
    content = content[:s9_start] + content[s10_end:]
    
    # Append them before the first <script> tag (like Section 8)
    script_idx = content.find('<script>')
    content = content[:script_idx] + sections_9_10 + '\n' + content[script_idx:]

# 2. Fix CSS Snow that is out of bounds
out_of_bounds_snow_start = content.find('<!-- CSS Snow/Ice Particles -->', content.find('</html>'))
if out_of_bounds_snow_start != -1:
    # Just remove it from the bottom
    content = content[:out_of_bounds_snow_start].strip() + '\n'

with open(filepath, 'w') as f:
    f.write(content)

