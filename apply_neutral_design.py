"""
Apply creating-comparison-tables skill to SD-WAN HTML
Removes colorful styling and implements neutral, fact-based design
"""

import re
from pathlib import Path

def apply_neutral_design(file_path):
    """Apply neutral comparison table design per skill guidelines"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # 1. Simplify table headers - remove colorful backgrounds
    # Replace colorful header backgrounds with neutral gray
    patterns = [
        (r'background-color:\s*#1e88e5', 'background-color: #f8fafc'),
        (r'background-color:\s*#2e7d32', 'background-color: #f8fafc'),
        (r'background-color:\s*#7b1fa2', 'background-color: #f8fafc'),
        (r'background-color:\s*#43a047', 'background-color: #f8fafc'),
        (r'background-color:\s*#1976d2', 'background-color: #f8fafc'),
        (r'background-color:\s*#4caf50', 'background-color: #f8fafc'),
    ]
    
    for old, new in patterns:
        if re.search(old, content):
            content = re.sub(old, new, content)
            changes.append(f"Neutralized table header: {old[:30]}")
    
    # 2. Change white text in headers to dark text
    # Find th elements with white color and change to dark
    content = re.sub(
        r'(<th[^>]*color:\s*)white([^>]*>)',
        r'\1#1e293b\2',
        content
    )
    changes.append("Changed header text from white to dark gray")
    
    # 3. Remove gradient backgrounds from cards
    content = re.sub(
        r'background:\s*linear-gradient\([^)]+\)',
        'background: #ffffff',
        content
    )
    changes.append("Removed gradient backgrounds")
    
    # 4. Simplify scenario cards - remove colorful borders
    content = re.sub(
        r'border-left:\s*4px\s+solid\s+#[0-9a-fA-F]{6}',
        'border-left: 4px solid #e2e8f0',
        content
    )
    changes.append("Simplified card borders to neutral gray")
    
    # 5. Add clear section headers with simple styling
    # This will be done manually in specific locations
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changes

if __name__ == '__main__':
    import sys
    import io
    
    # Fix Windows console encoding
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    file_path = Path(r'C:\Users\toru.tanji\Documents\Projects\portal_git_backup\project_sd_wan.html')
    
    print("Applying neutral comparison design...")
    print(f"Target: {file_path}")
    print()
    
    changes = apply_neutral_design(file_path)
    
    print("Changes applied:")
    for i, change in enumerate(changes, 1):
        print(f"{i}. {change}")
    
    print()
    print(f"Successfully applied neutral design to {file_path}")
