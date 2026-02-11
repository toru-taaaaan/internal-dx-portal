# Portal Component Standards & Evidence Linking Guide

This document defines the standardized components for the Internal DX Portal.
Use these templates to ensure consistency across all project reports and strategy documents.

---

## 1. Standard Sticky Header

Every major report page must use this sticky header structure.
Replace `[Project Name]` and `[Update Message]` with specific content.

```html
<header class="bg-white border-b border-slate-200 shadow-sm sticky top-0 z-50">
    <div class="max-w-7xl mx-auto px-4 md:px-8 h-16 flex items-center justify-between">
        <div class="flex items-center gap-4">
            <a href="index.html"
                class="flex items-center gap-2 text-slate-500 hover:text-brand-navy transition-colors text-sm font-medium">
                <svg class="w-3 h-3 flex-shrink-0" style="width: 12px; height: 12px;" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2.5"
                        d="M10 19l-7-7m0 0l7-7m-7 7h18" />
                </svg>
                ポータルへ戻る
            </a>
            <div class="h-4 w-px bg-slate-300 mx-2" style="width: 1px; height: 16px; background-color: #cbd5e1;"></div>
            <span class="text-base font-bold text-slate-700">プロジェクト 15.xx: [Project Name]</span>
        </div>
        <div class="flex items-center gap-3">
            <span
                class="inline-flex items-center px-3 py-1 rounded-full text-sm font-medium bg-blue-50 text-blue-700 border border-blue-200">
                🔄 最終更新：[Update Message] (v2026xxxx_xxxx)
            </span>
        </div>
    </div>
</header>
```

---

## 2. Reference Materials (Evidence Section)

Every report citing costs, specs, or decisions must verify facts using the **Evidence Management Sheet**.
Append this section at the bottom of the content container (before the closing `</div>` and script tags).

### Step A: Define References
List your sources clearly. Use the `[x]` format.

```html
<section class="section-card" style="margin-top: 40px; border-top: 4px solid var(--border);">
    <div class="section-title">📚 参照資料 (Reference Materials)</div>
    <p style="font-size: 0.9rem; color: var(--text-muted); margin-bottom: 20px;">
        本報告書の数値および技術仕様は、以下のエビデンスに基づき作成されています。
    </p>
    <div style="font-size: 0.85rem; line-height: 1.8;">
        <!-- Example Entry -->
        <div style="margin-bottom: 12px;">
            <strong>[12] SECOM社 正式見積書 (37702512-007)</strong><br>
            <span style="color: var(--text-muted);">環境開放・アプリ設定費用 ¥198,000 の確定。</span>
        </div>
        <!-- Add more references here -->
    </div>
    
    <!-- Standard Footer Link to Evidence Sheet -->
    <div class="info-box" style="margin-top: 20px; font-size: 0.8rem; background: #f1f5f9;">
        <strong>💡 エビデンス管理について:</strong><br>
        詳細な引用箇所、ファイルパス、および上記以外の共通資料（オンプレミス台帳等）については、
        情報システム部内保存の <a href="file:///C:/Users/toru.tanji/Obsidian/SecondBrain_Final/01_Workspace/11_プロジェクト/15.01_AD_Cloud_Migration/00_エビデンス管理シート.md">00_エビデンス管理シート.md</a> を参照してください。
        本ポータルに掲載されている全ての情報は、上記管理シートにより「事実」として検証済みです。
    </div>
</section>
```

### Step B: Inline Verification
In the main text or tables, link strictly to these numbers using superscript.

```html
<!-- Example Usage -->
初期費用は ¥198,000<sup>[12]</sup> となります。
ダウンタイムは最大2時間<sup>[10]</sup>です。
```

---

## 3. Evidence Management Protocol

1. **Locate the Fact**: Find the exact quote/number in source PDFs or emails.
2. **Register in Obsidian**: Add the file path and quote to `00_エビデンス管理シート.md`.
3. **Assign ID**: Give it a sequential number (e.g., [16]).
4. **Implement in Portal**: Use the ID in the HTML as shown above.

**Master Evidence Sheet Path:**
`c:\Users\toru.tanji\Obsidian\SecondBrain_Final\01_Workspace\11_プロジェクト\15.01_AD_Cloud_Migration\00_エビデンス管理シート.md`
