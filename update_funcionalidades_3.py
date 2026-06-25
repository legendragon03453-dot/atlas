import re

with open('funcionalidades.html', 'r') as f:
    content = f.read()

# 1. Replace Vista da Montanha canvas with image
vista_pattern = re.compile(r'<div class="mt-4 rounded-xl border border-zinc-200 group-hover:border-\[#367CF5\]/40.*?</script>', re.DOTALL)
vista_replacement = '<div class="mt-6 rounded-xl overflow-hidden border border-zinc-200 shadow-sm"><img src="https://github.com/legendragon03453-dot/atlas/blob/main/ATLAS/IMG%207_1x.webp?raw=true" alt="Vista da Montanha" class="w-full h-auto"></div>'
content = vista_pattern.sub(vista_replacement, content, count=1)

# 2. Move badge and change text to "Recomendado"
# Remove badge from Pro and pro-card class
pro_pattern = re.compile(r'<!-- Pro -->\s*<div class="pricing-card pro-card p-8 flex flex-col justify-between" style="transition-delay: 100ms;">\s*<div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-\[#367CF5\] text-white text-xs font-bold px-4 py-1\.5 rounded-full shadow-sm uppercase tracking-wide whitespace-nowrap">\s*Seu plano atual\s*</div>')
pro_replacement = r'<!-- Pro -->\n                <div class="pricing-card p-8 flex flex-col justify-between" style="transition-delay: 100ms;">'
content = pro_pattern.sub(pro_replacement, content, count=1)

# Add badge and pro-card to Elite
elite_pattern = re.compile(r'<!-- Elite -->\s*<div class="pricing-card p-8 flex flex-col justify-between" style="transition-delay: 200ms;">')
elite_replacement = r'<!-- Elite -->\n                <div class="pricing-card pro-card p-8 flex flex-col justify-between" style="transition-delay: 200ms;">\n                    <div class="absolute -top-4 left-1/2 -translate-x-1/2 bg-[#367CF5] text-white text-xs font-bold px-4 py-1.5 rounded-full shadow-sm uppercase tracking-wide whitespace-nowrap">\n                        Recomendado\n                    </div>'
content = elite_pattern.sub(elite_replacement, content, count=1)

# 3. Disable table animation on mobile
# Find CSS and wrap .table-row-stagger and .check-pop in @media (min-width: 768px)
css_pattern = re.compile(r'(\.check-pop\s*\{[^}]*\}\s*\.table-row-stagger\s*\{[^}]*\})', re.DOTALL)
css_replacement = r'@media (min-width: 768px) {\n        \1\n        }'
content = css_pattern.sub(css_replacement, content, count=1)

# Update GSAP script to only run on desktop
js_pattern = re.compile(r'(// Animate rows\s*const rows = document\.querySelectorAll\(\'\.table-row-stagger\'\);)', re.DOTALL)
js_replacement = r'if (window.innerWidth >= 768) {\n                        \1'
content = js_pattern.sub(js_replacement, content, count=1)

js_close_pattern = re.compile(r'(delay: 0\.2\s*\}\);\s*\}\s*)(\}\s*\}\);\s*</script>)', re.DOTALL)
js_close_replacement = r'\1}\n                    \2'
content = js_close_pattern.sub(js_close_replacement, content, count=1)


with open('funcionalidades.html', 'w') as f:
    f.write(content)

print("Done")
