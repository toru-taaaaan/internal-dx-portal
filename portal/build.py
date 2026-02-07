import os
import shutil
import re

# Configuration
SOURCE_DIR = '.source'
DIST_DIR = 'dist'
LOCAL_DIR = 'local_preview'

def clean_directory(path):
    if os.path.exists(path):
        shutil.rmtree(path)
    os.makedirs(path)

def process_html_for_web(content):
    # For Web (GAS), we keep GAS specific tags like <?= include(...) ?>
    # Usually no change needed if the source is already GAS-ready
    return content

def process_html_for_local(content):
    # 1. Replace GAS includes with actual file content if possible, or mock it
    # Pattern: <?!= include('path/to/file'); ?>
    # For now, simplistic approach: change links to relative .html
    
    # Replace google.script.run with console.log mocks? (Advanced)
    
    # Simple link fix: href="?page=something" -> href="something.html"
    content = re.sub(r'href="\?page=([^"]+)"', r'href="\1.html"', content)
    
    return content

def build():
    print("Starting Build Process...")
    
    # 1. Clean Output Dirs
    clean_directory(DIST_DIR)
    clean_directory(LOCAL_DIR)
    
    # 2. Copy Assets (CSS, JS, Images) to both
    # Assuming assets are in .source/assets
    if os.path.exists(os.path.join(SOURCE_DIR, 'assets')):
        shutil.copytree(os.path.join(SOURCE_DIR, 'assets'), os.path.join(DIST_DIR, 'assets'))
        shutil.copytree(os.path.join(SOURCE_DIR, 'assets'), os.path.join(LOCAL_DIR, 'assets'))

    # 3. Process Files
    for root, dirs, files in os.walk(SOURCE_DIR):
        # Calculate relative path to maintain structure
        rel_path = os.path.relpath(root, SOURCE_DIR)
        
        # Skip assets folder in loop if handled above
        if 'assets' in rel_path:
            continue
            
        target_dist = os.path.join(DIST_DIR, rel_path)
        target_local = os.path.join(LOCAL_DIR, rel_path)
        
        if not os.path.exists(target_dist): os.makedirs(target_dist)
        if not os.path.exists(target_local): os.makedirs(target_local)

        for file in files:
            src_file_path = os.path.join(root, file)
            
            if file.endswith('.html'):
                with open(src_file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Web Build
                web_content = process_html_for_web(content)
                with open(os.path.join(target_dist, file), 'w', encoding='utf-8') as f:
                    f.write(web_content)
                    
                # Local Build
                local_content = process_html_for_local(content)
                with open(os.path.join(target_local, file), 'w', encoding='utf-8') as f:
                    f.write(local_content)
            else:
                # Just copy other files
                shutil.copy2(src_file_path, os.path.join(target_dist, file))
                shutil.copy2(src_file_path, os.path.join(target_local, file))

    print("Build Complete!")
    print(f"   - Web Distribution: {DIST_DIR}/")
    print(f"   - Local Preview:    {LOCAL_DIR}/")

if __name__ == '__main__':
    build()
