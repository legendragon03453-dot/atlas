import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Update Menu Navbar
content = content.replace(
    '<a href="#" class="hover:text-blue-200 transition-colors">Depoimentos</a>',
    '<a href="#" class="hover:text-blue-200 transition-colors">Funcionalidades</a>'
)

# 2. Update Footer Link
content = content.replace(
    '<a href="#" class="hover:text-white transition-colors">Depoimentos</a>',
    '<a href="#" class="hover:text-white transition-colors">Funcionalidades</a>'
)

# 3. Remove Twitter (the second SVG icon in the footer which is Twitter's bird-like path, or just look for the second block in social space-x-6)
# Actually, the second icon path starts with: d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723
twitter_icon = '<a href="#" class="w-10 h-10 rounded-full border border-white/20 flex items-center justify-center text-white hover:bg-white hover:text-[#367CF5] transition-all">\n                        <svg class="w-4 h-4" fill="currentColor" viewBox="0 0 24 24"><path d="M23.953 4.57a10 10 0 01-2.825.775 4.958 4.958 0 002.163-2.723c-.951.555-2.005.959-3.127 1.184a4.92 4.92 0 00-8.384 4.482C7.69 8.095 4.067 6.13 1.64 3.162a4.822 4.822 0 00-.666 2.475c0 1.71.87 3.213 2.188 4.096a4.904 4.904 0 01-2.228-.616v.06a4.923 4.923 0 003.946 4.827 4.996 4.996 0 01-2.212.085 4.936 4.936 0 004.604 3.417 9.867 9.867 0 01-6.102 2.105c-.39 0-.779-.023-1.17-.067a13.995 13.995 0 007.557 2.209c9.053 0 13.998-7.496 13.998-13.985 0-.21 0-.42-.015-.63A9.935 9.935 0 0024 4.59z" /></svg>\n                    </a>'
if twitter_icon in content:
    content = content.replace(twitter_icon, '')
else:
    print("Warning: could not find exact twitter icon string.")

with open(filepath, 'w') as f:
    f.write(content)

