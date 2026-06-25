import re

for filename in ['index.html', 'funcionalidades.html']:
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # 1. Fix the main section height
        content = content.replace('class="w-full bg-[#367CF5] min-h-[200vh] px-4 relative flex flex-col items-center"', 'class="w-full bg-[#367CF5] min-h-0 md:min-h-[200vh] px-4 relative flex flex-col items-center"')

        # 2. Fix the sticky heading container
        content = content.replace('class="sticky top-0 w-full h-[100vh] flex flex-col items-center justify-center z-0 pointer-events-none"', 'class="md:sticky md:top-0 w-full md:h-[100vh] flex flex-col items-center justify-center z-0 pointer-events-none py-16 md:py-0"')

        # 3. Fix the heading text padding
        content = content.replace('px-4 pb-[15vh]"', 'px-4 md:pb-[15vh] mb-8 md:mb-0"')

        # 4. Fix the cards container negative margin
        content = content.replace('class="w-full max-w-5xl mx-auto flex flex-col gap-8 md:gap-12 relative z-10 mt-[-70vh] pb-[30vh]"', 'class="w-full max-w-5xl mx-auto flex flex-col gap-8 md:gap-12 relative z-10 md:mt-[-70vh] pb-16 md:pb-[30vh]"')

        # Optional: Disable the CSS blur/opacity for mobile just in case, but actually let's just make the animation media query based if we want to be 100% safe.
        # It's better to just let the IntersectionObserver work since it's now in the normal document flow.

        with open(filename, 'w') as f:
            f.write(content)
            
    except FileNotFoundError:
        pass
