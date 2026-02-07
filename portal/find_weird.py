
import string

def find_weird_chars(filepath):
    with open(filepath, 'rb') as f:
        content = f.read()

    errors = []
    line_num = 1
    col_num = 1
    
    printable = set(string.printable.encode('ascii'))
    # Also allow standard Japanese characters (this is crude but works for spotting control chars)
    
    for i, byte in enumerate(content):
        if byte == ord('\n'):
            line_num += 1
            col_num = 1
            continue
            
        # Check for non-printable control characters (except maybe tab/cr/lf)
        if byte < 32 and byte not in [9, 10, 13]:
            errors.append(f"Line {line_num}, Col {col_num}: Control char {hex(byte)} found")
            
        col_num += 1

    return errors

if __name__ == "__main__":
    file_to_check = r'c:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\社内DXポータル\project_15_01.html'
    results = find_weird_chars(file_to_check)
    if not results:
        print("No weird control characters found.")
    else:
        for err in results:
            print(err)
