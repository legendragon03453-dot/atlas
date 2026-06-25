import re

filepath = "/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html"
with open(filepath, 'r') as f:
    content = f.read()

# Add GSAP intro animation
intro_script = """
        // GSAP: Animação de Entrada (Intro Load)
        const introTl = gsap.timeline();
        introTl.from("header", { y: -50, opacity: 0, duration: 1, ease: "power3.out" })
               .from("main h1", { y: 40, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.5")
               .from("main p", { y: 30, opacity: 0, duration: 1, ease: "power3.out" }, "-=0.7")
               .from("main button", { scale: 0.5, opacity: 0, duration: 0.8, ease: "back.out(1.7)" }, "-=0.6");
"""

# Insert right after DOMContentLoaded or gsap.registerPlugin(ScrollTrigger);
insert_marker = "gsap.registerPlugin(ScrollTrigger);"
if insert_marker in content:
    content = content.replace(insert_marker, insert_marker + "\n" + intro_script)

with open(filepath, 'w') as f:
    f.write(content)

