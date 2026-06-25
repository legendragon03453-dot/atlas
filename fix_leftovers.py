import re

def fix_leftovers(content):
    content = content.replace('#367CF5', '#1C5E91')
    content = content.replace('#367cf5', '#1C5E91')
    content = content.replace('rgba(54, 124, 245', 'rgba(28, 94, 145')
    
    # Wait, some might have been partially replaced like via-[#367CF5]/80
    content = content.replace('via-[#1C5E91]/80', 'via-atlas-blue/80')
    content = content.replace('stroke-[#1C5E91]', 'stroke-atlas-blue')
    
    return content

files = ['index.html', 'funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        content = fix_leftovers(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Fixed leftovers in {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename}")
