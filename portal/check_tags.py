
import re

def check_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Remove all comments
    content = re.sub(r'<!--.*?-->', '', content, flags=re.DOTALL)
    
    # Regex for all tags we care about, matching across lines
    tag_pattern = re.compile(r'<(/?)(main|section|div|table|thead|tbody|tr|th|td|h[1-6]|p|ul|ol|li|span|a|button|script|style|header|footer|head|body|html)\b([^>]*)>', re.IGNORECASE | re.DOTALL)

    stack = []
    errors = []
    
    # Find line numbers by counting newlines up to the match
    def get_line_num(pos):
        return content.count('\n', 0, pos) + 1

    for match in tag_pattern.finditer(content):
        is_closing = match.group(1) == '/'
        tag_name = match.group(2).lower()
        attributes = match.group(3)
        pos = match.start()
        line_num = get_line_num(pos)
        
        # Skip self-closing tags (check for / at end of attributes)
        if attributes.strip().endswith('/'):
            continue
            
        # Also skip standard self-closing tags
        if tag_name in ['img', 'br', 'hr', 'input', 'link', 'meta', 'base'] and not is_closing:
            continue
            
        if is_closing:
            if not stack:
                errors.append(f"Line {line_num}: Unexpected closing tag </{tag_name}>")
            else:
                last_tag, last_line = stack.pop()
                if last_tag != tag_name:
                    errors.append(f"Line {line_num}: Tag mismatch. Expected </{last_tag}> (from line {last_line}), found </{tag_name}>")
        else:
            stack.append((tag_name, line_num))

    for tag, line in reversed(stack):
        errors.append(f"Unclosed tag <{tag}> from line {line}")

    return errors

if __name__ == "__main__":
    file_to_check = r'c:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル\project_15_01.html'
    results = check_tags(file_to_check)
    if not results:
        print("No structural errors found.")
    else:
        for err in results:
            print(err)
