
import re

def analyze_nesting(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Regex for all tags we care about
    tag_pattern = re.compile(r'<(/?)(main|section|div)\b([^>]*)>', re.IGNORECASE | re.DOTALL)

    stack = []
    
    def get_line_num(pos):
        return content.count('\n', 0, pos) + 1

    print(f"{'Line':<6} | {'Depth':<5} | {'Action':<10} | {'Tag':<10} | {'Details'}")
    print("-" * 80)

    for match in tag_pattern.finditer(content):
        is_closing = match.group(1) == '/'
        tag_name = match.group(2).lower()
        attributes = match.group(3)
        pos = match.start()
        line_num = get_line_num(pos)
        
        if attributes.strip().endswith('/'):
            continue
            
        if is_closing:
            if stack:
                last_tag, last_line, last_depth = stack.pop()
                print(f"{line_num:<6} | {len(stack):<5} | CLOSE      | {tag_name:<10} | (opened at line {last_line})")
            else:
                print(f"{line_num:<6} | 0     | EXTRA CLOSE| {tag_name:<10}")
        else:
            # Extract ID if present for better identification
            id_match = re.search(r'id=["\'](.*?)["\']', attributes)
            class_match = re.search(r'class=["\'](.*?)["\']', attributes)
            details = ""
            if id_match: details += f"id={id_match.group(1)} "
            if class_match:
                classes = class_match.group(1).split()
                # Show first few classes to identify the div
                details += f"classes=[{', '.join(classes[:3])}]"
            
            print(f"{line_num:<6} | {len(stack):<5} | OPEN       | {tag_name:<10} | {details}")
            stack.append((tag_name, line_num, len(stack)))

    for tag, line, depth in reversed(stack):
        print(f"!!! | {depth:<5} | UNCLOSED   | {tag:<10} | (from line {line})")

if __name__ == "__main__":
    file_to_check = r'c:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル\project_15_01.html'
    analyze_nesting(file_to_check)
