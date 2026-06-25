import re

for filename in ['index.html', 'funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()
    
    # We need to replace `</nav>\s*</header>` with `</nav>\n    </div>\n</header>`
    content = re.sub(r'</nav>\s*</header>', '</nav>\n    </div>\n</header>', content)
    
    with open(filename, 'w') as f:
        f.write(content)
