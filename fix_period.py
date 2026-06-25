import re

def fix_period(content):
    # Add the missing period at the end of "Quando entende, age"
    content = content.replace(
        'Quando você vê seu futuro, entende por que economizar importa. Quando entende, age',
        'Quando você vê seu futuro, entende por que economizar importa. Quando entende, age.'
    )

    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_period(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
