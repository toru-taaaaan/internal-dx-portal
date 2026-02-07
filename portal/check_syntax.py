
import re

def check_syntax(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all tags
    tag_pattern = re.compile(r'<(/?[a-zA-Z0-9]+)([^>]*)', re.DOTALL)
    
    errors = []
    
    def get_line_num(pos):
        return content.count('\n', 0, pos) + 1

    for match in tag_pattern.finditer(content):
        tag_name = match.group(1)
        attrs = match.group(2)
        line_num = get_line_num(match.start())
        
        # Check for unclosed quotes in attributes
        # A simple check: count quotes. If odd, it's likely broken.
        double_quotes = attrs.count('"')
        single_quotes = attrs.count("'")
        
        if double_quotes % 2 != 0:
            errors.append(f"Line {line_num}: Unclosed double quote in tag <{tag_name}>")
        if single_quotes % 2 != 0:
            # Special case for JS oncilck which might use single quotes
            # But they should be balanced within the attribute
            errors.append(f"Line {line_num}: Unclosed single quote in tag <{tag_name}>")

        # Check for missing closing bracket before next tag
        # (This is harder, but look for < inside attrs)
        if '<' in attrs:
            errors.append(f"Line {line_num}: Possible missing '>' in tag <{tag_name}> (contains '<' in attributes)")

    return errors

if __name__ == "__main__":
    file_to_check = r'c:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル\project_15_01.html'
    results = check_syntax(file_to_check)
    if not results:
        print("No syntax errors found.")
    else:
        for err in results:
            print(err)
