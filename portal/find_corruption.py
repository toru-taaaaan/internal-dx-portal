
import re

def find_corrupted_tags(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex for tags spanning multiple lines with significant internal newlines
    # Look for characters between < and >
    tag_pattern = re.compile(r'<[a-zA-Z0-9]+[^>]+>', re.DOTALL)
    
    corrupted = []
    
    def get_line_num(pos):
        return content.count('\n', 0, pos) + 1

    for match in tag_pattern.finditer(content):
        tag = match.group(0)
        line_num = get_line_num(match.start())
        
        # Check if the tag contains more than, say, 2 newlines
        if tag.count('\n') > 2:
            # Check if there are large gaps (many newlines)
            if '\n\n\n' in tag:
                corrupted.append((line_num, tag))

    return corrupted

if __name__ == "__main__":
    file_to_check = r'c:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル\project_15_01.html'
    results = find_corrupted_tags(file_to_check)
    if not results:
        print("No corrupted tags found.")
    else:
        for line, tag in results:
            # Print first 50 chars of the tag and the newline count
            print(f"Line {line}: Tag with {tag.count('\n')} newlines! Start: {tag[:50]}...")
