import re

def fix_dashes(content):
    # Fix specific grammatical cases first
    content = content.replace(' — e ', ' e ')
    content = content.replace('— e ', ' e ')
    content = content.replace(' — sem', ', sem')
    content = content.replace('— sem', ', sem')
    content = content.replace(' — pra', ', pra')
    content = content.replace('— pra', ', pra')
    content = content.replace('Não — complementa', 'Não, complementa')
    content = content.replace('Não você adivinhando — você decidindo', 'Não você adivinhando, você decidindo')
    content = content.replace('Liberdade — curso', 'Liberdade, curso')
    content = content.replace('módulos — é', 'módulos, é')
    content = content.replace('— No segundo', 'No segundo')
    
    # Generic fallback: replace any remaining em-dashes surrounded by spaces with a comma and space
    content = content.replace(' — ', ', ')
    # Or just remove if still left
    content = content.replace('— ', ' ')
    content = content.replace(' —', ' ')
    content = content.replace('—', '')
    
    # Also fix title hyphens just in case
    content = content.replace('<title>Atlas - Toda montanha', '<title>Atlas | Toda montanha')

    return content

files = ['index.html', 'funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_dashes(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
