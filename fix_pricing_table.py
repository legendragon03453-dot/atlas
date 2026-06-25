import re

for filename in ['index.html', 'funcionalidades.html']:
    try:
        with open(filename, 'r') as f:
            content = f.read()

        # 1. Make the table visible on mobile by removing hidden lg:block
        # We also change the comment for clarity
        content = content.replace('<!-- Tabela Comparativa (Desktop Only) -->', '<!-- Tabela Comparativa (Responsive com Scroll Horizontal) -->')
        content = content.replace('<div class="hidden lg:block w-full mt-24">', '<div class="block w-full mt-16 lg:mt-24">')

        # 2. Add an overflow-x-auto wrapper and a min-width to the grid so it scrolls instead of squishing
        original_grid_start = '<div class="grid grid-cols-4 divide-x divide-zinc-200 border-t border-b border-zinc-200 bg-white shadow-sm rounded-xl overflow-hidden text-sm">'
        
        # We wrap it in a div that allows horizontal scroll, and add min-w-[700px] or min-w-[800px] to the grid itself
        # Also added custom scrollbar classes for better mobile UX if needed, but standard overflow-x-auto is fine.
        new_grid_start = '''<div class="w-full overflow-x-auto pb-4 snap-x">
                    <div class="min-w-[700px] grid grid-cols-4 divide-x divide-zinc-200 border-t border-b border-zinc-200 bg-white shadow-sm rounded-xl overflow-hidden text-sm">'''
        
        content = content.replace(original_grid_start, new_grid_start)

        # 3. We must close the new wrapper div at the end of the table
        # Find where the grid ends. 
        # The grid ends right before: </div> <!-- End of Tabela wrapper -->
        # Let's find the exact string.
        # It's followed by: </section>
        # Let's use regex to find the end of the grid and insert the closing </div>
        
        # Looking at lines 1361-1368:
        #                     <div class="p-4 flex justify-center items-center"><svg class="w-5 h-5 text-[#367CF5]" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"></path></svg></div>
        #
        #                 </div>
        #             </div>
        #
        #         </div>
        #     </section>
        
        # This is slightly tricky, we can just replace the closing tags.
        original_closing = '''
                </div>
            </div>

        </div>
    </section>'''
        
        new_closing = '''
                </div>
                </div> <!-- Fechamento do overflow-x-auto -->
            </div>

        </div>
    </section>'''
        
        content = content.replace(original_closing, new_closing)

        with open(filename, 'w') as f:
            f.write(content)
            
    except FileNotFoundError:
        pass
