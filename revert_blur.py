import re

for filename in ['/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', '/Users/lippo/.gemini/antigravity/scratch/atlas-website/funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()

    css_to_remove = """
        /* Vignette Blur Effect */
        .blur-overlay-top {
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 12vh;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            mask-image: linear-gradient(to bottom, black 0%, transparent 100%);
            -webkit-mask-image: linear-gradient(to bottom, black 0%, transparent 100%);
            z-index: 5;
            pointer-events: none;
        }
        .blur-overlay-bottom {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            height: 12vh;
            backdrop-filter: blur(6px);
            -webkit-backdrop-filter: blur(6px);
            mask-image: linear-gradient(to top, black 0%, transparent 100%);
            -webkit-mask-image: linear-gradient(to top, black 0%, transparent 100%);
            z-index: 5;
            pointer-events: none;
        }
"""
    content = content.replace(css_to_remove, "")
    
    html_blur_divs = """<!-- Fisheye Blur Overlays -->
    <div class="blur-overlay-top"></div>
    <div class="blur-overlay-bottom"></div>"""
    content = content.replace(html_blur_divs, "")

    with open(filename, 'w') as f:
        f.write(content)

