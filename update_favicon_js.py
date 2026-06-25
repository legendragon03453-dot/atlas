import re
import os

def fix_favicon(content):
    # Remove existing favicon link
    content = re.sub(r'<link rel="icon".*?>\n?', '', content)
    
    favicon_script = """    <!-- Dynamic Favicon -->
    <script>
        (function() {
            function updateFavicon() {
                const isDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
                const canvas = document.createElement('canvas');
                const ctx = canvas.getContext('2d');
                const img = new Image();
                img.crossOrigin = "Anonymous";
                
                img.onload = function() {
                    canvas.width = img.width || 32;
                    canvas.height = img.height || 32;
                    
                    if (isDark) {
                        // In dark mode, we want a white logo. The original is black.
                        ctx.filter = 'brightness(0) invert(1)';
                    } else {
                        // In light mode, we want a black logo.
                        ctx.filter = 'brightness(0)';
                    }
                    
                    ctx.drawImage(img, 0, 0);
                    
                    let link = document.querySelector("link[rel*='icon']");
                    if (!link) {
                        link = document.createElement('link');
                        link.rel = 'icon';
                        document.head.appendChild(link);
                    }
                    link.type = 'image/png';
                    try {
                        link.href = canvas.toDataURL('image/png');
                    } catch (e) {
                        console.error("Favicon canvas taint error", e);
                        // Fallback to direct image
                        link.href = img.src;
                    }
                };
                // Using raw.githubusercontent.com for proper CORS headers
                img.src = "https://raw.githubusercontent.com/legendragon03453-dot/atlas/main/export_2026-06-04T03_26_23-606Z/Group%201_1x.webp";
            }

            if (document.readyState === "loading") {
                document.addEventListener("DOMContentLoaded", updateFavicon);
            } else {
                updateFavicon();
            }
            
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', updateFavicon);
        })();
    </script>
"""
    
    # Insert before closing </head>
    if "</head>" in content and "updateFavicon" not in content:
        content = content.replace("</head>", favicon_script + "</head>")
        
    return content

html_files = [f for f in os.listdir('.') if f.endswith('.html')]

for filename in html_files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
            
        new_content = fix_favicon(content)
        
        if new_content != content:
            with open(filename, 'w') as f:
                f.write(new_content)
            print(f"Successfully processed {filename}")
        else:
            print(f"No changes made in {filename}")
            
    except FileNotFoundError:
        pass
