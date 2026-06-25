import re

for filename in ['index.html', 'funcionalidades.html']:
    with open(filename, 'r') as f:
        content = f.read()

    # Original button string:
    # class="btn-green text-[#1A2E05] py-8 md:px-28 md:py-8 rounded-full font-black text-4xl md:text-5xl flex items-center justify-center gap-5 w-full sm:w-[80%] md:w-auto uppercase tracking-wide"
    
    # We will replace it with a smaller mobile version that has px-10 (padding left/right) and py-5 (padding top/bottom), text-2xl, w-auto
    original_btn = 'class="btn-green text-[#1A2E05] py-8 md:px-28 md:py-8 rounded-full font-black text-4xl md:text-5xl flex items-center justify-center gap-5 w-full sm:w-[80%] md:w-auto uppercase tracking-wide"'
    new_btn = 'class="btn-green text-[#1A2E05] py-4 px-8 md:px-28 md:py-8 rounded-full font-black text-2xl md:text-5xl inline-flex items-center justify-center gap-4 md:gap-5 w-auto uppercase tracking-wide"'
    
    # We also might want to check if the button has a slightly different class string, so we can use regex if needed
    # But let's try direct replace first
    if original_btn in content:
        content = content.replace(original_btn, new_btn)
    else:
        # Fallback regex just in case
        pattern = re.compile(r'class="btn-green text-\[#1A2E05\][^"]+"')
        content = pattern.sub(new_btn, content)

    with open(filename, 'w') as f:
        f.write(content)
