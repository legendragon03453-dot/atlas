import re

with open('index.html', 'r') as f:
    content = f.read()

# Remove the "Funcionalidade Essencial X" lines
content = re.sub(r'<li class="flex items-start gap-3">.*?Funcionalidade Essencial.*?</li>\n*', '', content)

with open('index.html', 'w') as f:
    f.write(content)

