import re

with open('index.html', 'r') as f:
    content = f.read()

# We want to remove the closing of DOMContentLoaded at line 1630 and move it to the end.
# Wait, the best way is just to replace the whole bottom script block with a nicely formatted version.

# Find the start of the bottom script block
start_idx = content.find("gsap.registerPlugin(ScrollTrigger);")

# We know DOMContentLoaded ends right before this: `        });\n\n        gsap.registerPlugin`
# Let's find that.
match = re.search(r'        \}\);\n            \}\);\n        \}\);\n\n        gsap\.registerPlugin', content)
if match:
    # Remove the closing `});`
    # Actually let's just do a string replace of `            });\n        });\n\n        gsap.registerPlugin(ScrollTrigger);`
    pass

# A cleaner way is to rewrite everything from `gsap.registerPlugin(ScrollTrigger);` to `</script>`
# And wrap it in the `DOMContentLoaded` that was closed prematurely.

old_block = """                    }
                });
            });
        });

        gsap.registerPlugin(ScrollTrigger);"""

new_block = """                    }
                });
            });

        gsap.registerPlugin(ScrollTrigger);"""

content = content.replace(old_block, new_block)

end_script_idx = content.rfind("</script>")
insert_code = """

        // Animação de Scroll Reveal
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

        }); // Fim do DOMContentLoaded
"""

content = content[:end_script_idx] + insert_code + content[end_script_idx:]

with open('index.html', 'w') as f:
    f.write(content)

