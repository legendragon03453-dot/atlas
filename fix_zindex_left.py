import re

for filename in ['index.html', 'funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()

    # Replace z-[9999] with z-50 and add left-0
    content = content.replace('class="fixed top-0 w-full flex justify-center z-[9999]', 'class="fixed top-0 left-0 w-full flex justify-center z-50')
    content = content.replace('class="fixed top-0 w-full flex justify-center z-[99]', 'class="fixed top-0 left-0 w-full flex justify-center z-50')

    with open(filename, 'w') as f:
        f.write(content)
