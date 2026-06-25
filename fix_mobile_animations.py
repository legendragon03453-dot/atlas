with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove 'scroll-reveal' from the hero h1 so it never hides
content = content.replace('scroll-reveal', '')

# 2. Fix the Mobile Navbar to have absolute max z-index
content = content.replace('z-[99]', 'z-[9999]')

# 3. Disable all javascript animations on mobile
# We can just inject a global check at the start of the DOMContentLoaded that wraps the whole animation logic
# Or simply remove the IntersectionObservers completely for mobile
# Let's completely remove the block:
# if (window.innerWidth < 768) { document.querySelectorAll('section > h2, section > div > h2, .scroll-reveal')... }
import re
observer_pattern = re.compile(r'// Animate section headings and cards on mobile.*?if \(window\.innerWidth < 768\) \{.*?\}\s*\}\)\(\);', re.DOTALL)
content = observer_pattern.sub('})();', content)

# 4. Wrap GSAP in desktop only
gsap_original = """gsap.utils.toArray('.scroll-reveal').forEach(element => {
            gsap.fromTo(element, 
                { y: 50, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: element,
                        start: "top 85%",
                        toggleActions: "play none none reverse"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 0.8,
                    ease: "power3.out"
                }
            );
        });"""

gsap_new = """if(window.innerWidth >= 768) {
        gsap.utils.toArray('.scroll-reveal').forEach(element => {
            gsap.fromTo(element, 
                { y: 50, opacity: 0 },
                {
                    scrollTrigger: {
                        trigger: element,
                        start: "top 85%",
                        toggleActions: "play none none reverse"
                    },
                    y: 0,
                    opacity: 1,
                    duration: 0.8,
                    ease: "power3.out"
                }
            );
        });
        }"""

content = content.replace(gsap_original, gsap_new)

with open('index.html', 'w') as f:
    f.write(content)
