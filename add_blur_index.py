import re

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'r') as f:
    content = f.read()

# 1. Inject the blur CSS
css_to_inject = """
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
    </style>
"""
if ".blur-overlay-top" not in content:
    content = content.replace('</style>', css_to_inject)

# 2. Inject the blur HTML divs right after <body>
html_blur_divs = """<body class="bg-zinc-50 text-zinc-900 font-sans">
    <!-- Fisheye Blur Overlays -->
    <div class="blur-overlay-top"></div>
    <div class="blur-overlay-bottom"></div>
"""
if "blur-overlay-top" not in content.split('<body')[1]:
    content = content.replace('<body class="bg-zinc-50 text-zinc-900 font-sans">', html_blur_divs)

with open('/Users/lippo/.gemini/antigravity/scratch/atlas-website/index.html', 'w') as f:
    f.write(content)

