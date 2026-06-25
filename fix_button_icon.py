import re

def fix_button_icon(content):
    # Change the icon inside the "Assinar Atlas" buttons to be white and slightly adjusted down
    content = content.replace(
        'class="h-4 md:h-5 filter brightness-0"',
        'class="h-5 md:h-6 filter brightness-0 invert opacity-90 mt-[2px] md:mt-1"'
    )
    return content

files = ['index.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        content = fix_button_icon(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
