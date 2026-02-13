"""
Complete neutral design - remove ALL colors and ensure readability
"""

import re
from pathlib import Path

def complete_neutralization(file_path):
    """Remove all remaining colors and ensure text readability"""
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    changes = []
    
    # 1. Remove ALL background colors except white and light gray
    # Replace any colored backgrounds
    color_patterns = [
        r'background-color:\s*#[0-9a-fA-F]{6}(?!;)',
        r'background:\s*#[0-9a-fA-F]{6}(?!;)',
    ]
    
    for pattern in color_patterns:
        matches = re.findall(pattern, content)
        for match in matches:
            # Extract the color
            color = re.search(r'#[0-9a-fA-F]{6}', match).group()
            # Only keep white, very light grays, and dark grays for text
            if color.lower() not in ['#ffffff', '#f8fafc', '#f9f9f9', '#fafafa', '#1e293b', '#64748b', '#e2e8f0']:
                # Replace with white or light gray
                if 'background' in match:
                    content = content.replace(match, match.replace(color, '#ffffff'))
                    changes.append(f"Removed color {color}")
    
    # 2. Ensure all text is dark gray or black
    # Replace any light colored text with dark gray
    content = re.sub(
        r'(color:\s*)#[0-9a-fA-F]{6}',
        lambda m: m.group(1) + '#1e293b' if not any(c in m.group(0) for c in ['#1e293b', '#64748b', '#ffffff']) else m.group(0),
        content
    )
    changes.append("Ensured all text is dark colored")
    
    # 3. Remove colored borders except neutral gray
    content = re.sub(
        r'border(?:-\w+)?:\s*\d+px\s+solid\s+#(?![e2e8f0|1e293b])[0-9a-fA-F]{6}',
        'border: 1px solid #e2e8f0',
        content
    )
    changes.append("Neutralized all borders")
    
    # 4. Fix Executive Summary - make it simple dark header
    content = re.sub(
        r'background:\s*linear-gradient[^;]+;',
        'background: #1e293b;',
        content
    )
    changes.append("Simplified Executive Summary background")
    
    # 5. Remove any remaining rgba colors
    content = re.sub(
        r'rgba\(\d+,\s*\d+,\s*\d+,\s*[\d.]+\)',
        'rgba(255, 255, 255, 0.1)',
        content
    )
    changes.append("Neutralized rgba colors")
    
    # Write back
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changes

if __name__ == '__main__':
    import sys
    import io
    
    if sys.platform == 'win32':
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
    
    file_path = Path(r'C:\Users\toru.tanji\Documents\Projects\portal_git_backup\project_sd_wan.html')
    
    print("Completing neutral design...")
    print()
    
    changes = complete_neutralization(file_path)
    
    print("Additional changes:")
    for i, change in enumerate(changes, 1):
        print(f"{i}. {change}")
    
    print()
    print("Complete neutralization finished")
