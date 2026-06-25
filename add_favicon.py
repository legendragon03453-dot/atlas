import re

favicon_tag = '<link rel="icon" type="image/webp" href="https://github.com/legendragon03453-dot/atlas/blob/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp?raw=true">'

for filename in ['index.html', 'funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()

    # If it already has a favicon, replace it, else add it after title
    if '<link rel="icon"' not in content:
        content = re.sub(r'(<title>.*?</title>)', r'\1\n    ' + favicon_tag, content, count=1)
    else:
        content = re.sub(r'<link rel="icon"[^>]+>', favicon_tag, content)

    with open(filename, 'w') as f:
        f.write(content)
