import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# 1. Fix Navbar CSS
old_mobile_nav = """        @media (max-width: 768px) {
            .navbar-shape {
                width: 100%;
                clip-path: polygon(0 0, 100% 0, 95% 100%, 5% 100%);
                padding: 1rem 2rem;
                flex-direction: column;
                gap: 1rem;
            }
            .nav-links {
                display: none; /* Esconder links em telas muito pequenas, precisaria de um menu hamburger real */
            }
        }"""

new_mobile_nav = """        @media (max-width: 768px) {
            .navbar-shape {
                width: 95%;
                clip-path: none;
                border-radius: 100px;
                padding: 0.5rem 1.5rem;
                flex-direction: row;
                justify-content: space-between;
                height: 60px;
                top: 10px;
            }
            .nav-links {
                display: none;
            }
            .navbar-shape .btn-nav {
                height: 36px;
                padding: 0 1rem;
                font-size: 12px;
                clip-path: none;
                border-radius: 100px;
            }
            .navbar-shape img {
                height: 24px;
            }
        }"""
content = content.replace(old_mobile_nav, new_mobile_nav)


# 2. Fix Section Paddings (Generic Replace)
content = content.replace('py-24 md:py-32', 'py-16 md:py-32')
content = content.replace('py-24 md:py-40', 'py-16 md:py-40')
content = content.replace('py-20 lg:py-32', 'py-16 lg:py-32')
content = content.replace('pt-24 pb-32', 'pt-16 pb-20 md:pt-24 md:pb-32')
content = content.replace('pt-32 pb-0', 'pt-20 md:pt-32 pb-0')

# 3. Fix Section 7 Gap
content = content.replace('gap-16 lg:gap-24', 'gap-10 lg:gap-24')

# 4. Fix Section 6 title 
content = content.replace('text-4xl md:text-5xl lg:text-6xl', 'text-3xl md:text-5xl lg:text-6xl')

# 5. Fix Section 8 title
# it's already 'text-4xl md:text-5xl lg:text-6xl', let's make it 'text-3xl md:text-5xl lg:text-6xl'
# Wait, Section 8 is: text-4xl md:text-5xl lg:text-6xl
# We already did replace for that.

# 6. Fix Section 10 title
content = content.replace('text-5xl md:text-7xl', 'text-4xl md:text-6xl lg:text-7xl')

# 7. Section 7 quote text
content = content.replace('text-3xl md:text-4xl', 'text-2xl md:text-4xl')

# 8. Add meta viewport if not present (it is present: <meta name="viewport" content="width=device-width, initial-scale=1.0">)

# 9. Fix FAQ title size
content = content.replace('text-4xl md:text-5xl lg:text-6xl', 'text-3xl md:text-5xl lg:text-6xl') # This will apply to both if not matched above

with open(filepath, 'w') as f:
    f.write(content)

