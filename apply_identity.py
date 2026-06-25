import re

def inject_tailwind_config(content):
    config_script = """    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        atlas: {
                            blue: '#1C5E91',
                            bg: '#FDF4E8',
                            green: '#1E613E',
                            red: '#B82B26',
                            yellow: '#F2AB0C',
                            dark: '#040C11',
                            lightBlue: '#69A0C1',
                            lightGreen: '#72B28F',
                            beige: '#EFCA71',
                            pink: '#D37976'
                        }
                    }
                }
            }
        }
    </script>"""
    # Inject after the tailwindcdn script
    return content.replace('<script src="https://cdn.tailwindcss.com"></script>', 
                         '<script src="https://cdn.tailwindcss.com"></script>\n' + config_script)

def apply_new_identity(content):
    # 1. Primary Blue replacements
    content = content.replace('bg-[#367CF5]', 'bg-atlas-blue')
    content = content.replace('text-[#367CF5]', 'text-atlas-blue')
    content = content.replace('border-[#367CF5]', 'border-atlas-blue')
    content = content.replace('ring-[#367CF5]', 'ring-atlas-blue')
    content = content.replace('from-[#367CF5]', 'from-atlas-blue')
    content = content.replace('to-[#367CF5]', 'to-atlas-blue')
    # Replace blue-500 and blue-600 used in gradients or generic buttons to the new primary
    content = content.replace('bg-blue-600', 'bg-atlas-blue')
    content = content.replace('hover:bg-blue-700', 'hover:bg-atlas-blue/90')
    content = content.replace('text-blue-500', 'text-atlas-blue')
    content = content.replace('text-blue-600', 'text-atlas-blue')
    
    # 2. Text colors to Dark
    content = content.replace('text-[#1a1a1a]', 'text-atlas-dark')
    content = content.replace('text-zinc-900', 'text-atlas-dark')
    content = content.replace('text-[#0F172A]', 'text-atlas-dark')
    content = content.replace('text-[#0B1A30]', 'text-atlas-dark')
    
    # 3. Section Backgrounds
    # Replace section backgrounds explicitly to avoid replacing small cards accidentally
    content = content.replace('class="w-full bg-white ', 'class="w-full bg-atlas-bg ')
    content = content.replace('class="w-full bg-[#FAF8F5] ', 'class="w-full bg-atlas-bg ')
    content = content.replace('<body class="bg-zinc-50 ', '<body class="bg-atlas-bg ')
    content = content.replace('bg-[#eff4ff]', 'bg-atlas-lightBlue/10')
    content = content.replace('bg-blue-50', 'bg-atlas-lightBlue/10')
    content = content.replace('bg-blue-100', 'bg-atlas-lightBlue/20')
    content = content.replace('border-blue-200', 'border-atlas-lightBlue/30')
    
    # 4. Success / Positive tags to Green
    # We had text-green-600 and bg-green-100 in Atlas Score
    content = content.replace('text-green-600', 'text-atlas-green')
    content = content.replace('bg-green-100', 'bg-atlas-lightGreen/30')
    
    # 5. Fix body CSS background fallback (in style tag)
    content = content.replace('background-color: #367CF5;', 'background-color: #1C5E91;')

    return content

files = ['index.html', 'funcionalidades.html']
for filename in files:
    try:
        with open(filename, 'r') as f:
            content = f.read()
        
        # Only inject if not already injected
        if 'tailwind.config =' not in content:
            content = inject_tailwind_config(content)
            
        content = apply_new_identity(content)
        
        with open(filename, 'w') as f:
            f.write(content)
        print(f"Successfully processed {filename}")
    except FileNotFoundError:
        print(f"Skipping {filename} - not found")
