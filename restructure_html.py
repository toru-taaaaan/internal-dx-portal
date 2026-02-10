"""
SD-WAN comparison HTML file restructuring script
Implements two-part narrative structure and professional language improvements
"""

import re
from pathlib import Path

def restructure_html(file_path):
    """Restructure HTML file into two-part narrative with professional language"""
    
    # Read the file with UTF-8 encoding
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Track changes
    changes = []
    
    # 1. Replace casual expressions with professional language
    replacements = [
        # Glossary title
        ('知っておきたい用語解説', '技術用語の解説'),
        
        # Remove "徹底" (thorough/exhaustive) - too casual
        ('仕組みの徹底比較', '技術的比較分析'),
        ('徹底比較', '比較分析'),
        
        # Replace "最強" (strongest) with more professional terms
        ('国内最強バックボーン', '国内最大級のバックボーン'),
        ('国内最強', '国内最大級'),
        
        # Replace casual questioning style
        ('なぜCatoは「次世代」と呼ばれるのか？ なぜIIJは「国内最強」なのか？', 
         '両ソリューションの技術的特徴と設計思想の違いを解説します。'),
        
        # Replace "現代的な設計"
        ('現代的な設計', '最新のアーキテクチャ'),
        
        # Replace competitive language
        ('第1ラウンドを勝ち抜いた', ''),
        ('黒船', ''),
        ('一騎打ち', '比較'),
    ]
    
    for old, new in replacements:
        if old in content:
            content = content.replace(old, new)
            changes.append(f"✓ Replaced '{old[:30]}...' with '{new[:30]}...'")
    
    # 2. Add Part 1 header before scenario comparison
    # Find the location before "シナリオ① 現状維持"
    part1_header = '''
        <!-- ========================================
             PART 1: 現状システムの課題分析
             ======================================== -->
        <div style="background: linear-gradient(135deg, #e3f2fd 0%, #bbdefb 100%); border-radius: var(--radius-lg); padding: 30px; margin: 60px 0 40px 0; border-left: 6px solid #1976d2; box-shadow: var(--shadow-md);">
            <h2 style="margin: 0 0 10px 0; font-size: 1.6rem; font-weight: 800; color: #0d47a1;">
                Part 1: 現状システムの課題と移行の必要性
            </h2>
            <p style="margin: 0; font-size: 1rem; color: #1565c0; line-height: 1.6;">
                USEN Vario Secureの現状を分析し、セキュリティ強化オプションの追加を含めた各シナリオを評価します。<br>
                この分析により、次世代ネットワークへの移行が必要であることを示します。
            </p>
        </div>

        <section style="margin-bottom: 60px;">
            <h3 style="color: #1976d2; margin-bottom: 20px; font-size: 1.3rem; border-bottom: 2px solid #1976d2; padding-bottom: 10px;">
                シナリオ比較: 現状維持 vs 強化 vs 刷新
            </h3>
            <p style="margin-bottom: 30px; color: #555; line-height: 1.6;">
                現在のUSEN Vario Secureを基準に、3つのシナリオを比較検討します。
            </p>
'''
    
    # Find pattern before scenario cards
    scenario_pattern = r'(<div style="display: grid; grid-template-columns: repeat\(3, 1fr\); gap: 15px; margin-bottom: 30px;">)'
    if re.search(scenario_pattern, content):
        content = re.sub(scenario_pattern, part1_header + r'\1', content, count=1)
        changes.append("✓ Added Part 1 header before scenario comparison")
    
    # 3. Add Part 2 header before IIJ料金表
    part2_header = '''
        </section>

        <!-- ========================================
             PART 2: 次世代ソリューションの比較分析
             ======================================== -->
        <div style="background: linear-gradient(135deg, #f3e5f5 0%, #e1bee7 100%); border-radius: var(--radius-lg); padding: 30px; margin: 60px 0 40px 0; border-left: 6px solid #7b1fa2; box-shadow: var(--shadow-md);">
            <h2 style="margin: 0 0 10px 0; font-size: 1.6rem; font-weight: 800; color: #4a148c;">
                Part 2: 次世代ソリューションの比較分析
            </h2>
            <p style="margin: 0; font-size: 1rem; color: #6a1b9a; line-height: 1.6;">
                IIJ Omnibus と Cato Cloud という2つの次世代SD-WANソリューションを、<br>
                コスト・機能・運用・拡張性など多角的な視点から客観的に比較します。
            </p>
        </div>

        <section style="margin-bottom: 60px;">
'''
    
    # Find IIJ料金表 section
    iij_pattern = r'(<h3[^>]*>.*?IIJ Omnibus.*?料金.*?</h3>)'
    if re.search(iij_pattern, content, re.DOTALL):
        content = re.sub(iij_pattern, part2_header + r'\1', content, count=1)
        changes.append("✓ Added Part 2 header before IIJ pricing section")
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(content)
    
    return changes

if __name__ == '__main__':
    file_path = Path(r'C:\Users\toru.tanji\Documents\Projects\portal_git_backup\project_sd_wan.html')
    
    print("Starting HTML restructuring...")
    print(f"Target file: {file_path}")
    print()
    
    changes = restructure_html(file_path)
    
    print("Changes applied:")
    for change in changes:
        print(change)
    
    print()
    print(f"✅ Successfully restructured {file_path}")
