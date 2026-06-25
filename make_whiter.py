import re

with open('index.html', 'r') as f:
    content = f.read()

# Replace the dark colors with lighter, whiter glassmorphism

# 1. Update card container: add backdrop-blur-md and bg-white/10, increase border
content = content.replace('shadow-[0_20px_40px_rgba(0,0,0,0.4)] border border-white/5', 'shadow-2xl border border-white/20 bg-white/10 backdrop-blur-md')

# 2. Update Left column: bg-[#1e293b] -> bg-white/5
content = content.replace('bg-[#1e293b] flex items-center justify-center', 'bg-white/5 flex items-center justify-center')

# 3. Update Middle column: bg-[#18181b] -> bg-white/5
content = content.replace('bg-[#18181b] flex flex-col', 'bg-white/5 flex flex-col')

# 4. Update Right column: bg-[#1e293b] -> bg-white/20
content = content.replace('bg-[#1e293b] flex flex-col', 'bg-white/20 flex flex-col')

with open('index.html', 'w') as f:
    f.write(content)
