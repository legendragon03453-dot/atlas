import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'r') as f:
    content = f.read()

# The block to remove:
block_regex = r'<!-- Menu Mobile Overlay -->.*?</div>'
# Find all occurrences
matches = re.findall(block_regex, content, flags=re.DOTALL)

if len(matches) > 1:
    # Remove all except the first one
    for match in matches[1:]:
        content = content.replace(match, '', 1)

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html', 'w') as f:
    f.write(content)

