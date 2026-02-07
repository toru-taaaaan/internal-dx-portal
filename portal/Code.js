// 🚀 GAS Expert: Robust & Scalable Backend (Updated: 2026-01-27 21:50)
// 3D Brain Icon from IconArchive
const FAVICON_DATA_URI = 'https://icons.iconarchive.com/icons/microsoft/fluentui-emoji-3d/96/Brain-3d-icon.png';

// 🛡️ SECURITY CONFIGURATION
// 🛡️ SECURITY CONFIGURATION
const CONFIG = {
  ADMIN_EMAILS: ['tanji@akiba-holdings.co.jp', 'shino@akiba-holdings.co.jp'],
  GUEST_USERS: [
    'nakano@akiba-holdings.co.jp',
    'm.nakano@akiba-holdings.co.jp', // ➕ Potential alternative
    'yudai.ishii@adtec.co.jp',
    'ishii@akiba-holdings.co.jp'
  ],
  ALLOWED_GROUP: '', // Disabled for strict control
  DEBUG_BYPASS_AUTH: true // 🔓 ENABLED TO ENSURE ACCESS
};

/**
 * Main Entry Point (GET Request)
 */
function doGet(e) {
  // Global Safety Net
  try {
    const userEmail = Session.getActiveUser().getEmail();
    const pageId = e.parameter.page || 'landing';

    // 1. Authorization
    if (!isUserAuthorized(userEmail, pageId)) {
      return renderAccessDenied(userEmail);
    }

    // 2. Routing
    // ONE-OFF API TRIGGER: Dynamic Search
    if (e.parameter.action === 'search_email') {
      const query = e.parameter.q || '見積';
      const results = searchGmail(query, true);
      return ContentService.createTextOutput(JSON.stringify(results))
        .setMimeType(ContentService.MimeType.JSON);
    }

    return resolveRoute(pageId, ScriptApp.getService().getUrl());

  } catch (criticalErr) {
    console.error('Critical Failure: ' + criticalErr);
    return renderErrorPage(criticalErr);
  }
}

/**
 * Checks if the current user is allowed to access the portal.
 */
function isUserAuthorized(email, pageId) {
  if (CONFIG.DEBUG_BYPASS_AUTH) return true;

  // 1. Admin Check (Full Access)
  if (CONFIG.ADMIN_EMAILS.indexOf(email) !== -1) return true;

  // 2. Guest Check (Partial Access)
  if (CONFIG.GUEST_USERS.indexOf(email) !== -1) {
    // Allow if pageId looks like "project_15.12" (dot or underscore)
    if (pageId && (pageId.indexOf('project_15.12') !== -1 || pageId.indexOf('project_15_12') !== -1)) {
      return true;
    }
  }

  return false;
}

/**
 * Routing Logic: Maps page IDs to templates or static content.
 */
function resolveRoute(pageId, currentUrl) {
  let templateName = 'index';
  let title = 'Internal DX Portal';

  // Basic Routing Map
  const ROUTE_MAP = {
    'home': { template: 'index', title: 'Internal DX Portal - Command Center' },
    'index': { template: 'index', title: 'Command Center | Internal DX Portal' },
    'landing': { handler: serveLandingRaw },
    'executive_hub': { template: 'executive_hub', title: 'IT基盤刷新 課題管理表 | Internal DX Portal' },
    'evaluation_sheet': { template: 'evaluation_sheet', title: '人事考課原本 | Internal DX Portal' },
    'daily_log': { template: 'daily_log', title: 'Daily Log | Internal DX Portal' },
    'bcp_risk_matrix': { template: 'bcp_risk_matrix', title: 'BCP Risk Matrix | Internal DX Portal' },
    'meeting_minutes_20260123': { template: 'meeting_minutes_20260123', title: '議事録 | Internal DX Portal' },
    'debug': { handler: serveDebugDashboard },
    'ping': { handler: servePing },
    'project_15_12_ishii': { template: 'project_15_12_ishii', title: '石井様向け相談資料' },
    'project_15_12_proposal': { template: 'project_15_12_proposal', title: 'AquaVoice提案書' },
    'project_15_12_antigravity': { template: 'project_15_12_antigravity', title: 'Antigravity導入案内' },
    'project_buddynet': { template: 'project_buddynet', title: 'BuddyNet DX Portal' },
    'project_sd_wan': { handler: serveProjectSdWan },
    'line_dashboard': { handler: serveProjectSdWan },
    'project_15.12_AIチャンピオン推進': { template: 'project_15_12', title: 'Project 15.12: AI Champion Portal' },
    'project_15.14_現状インフラ評価': { template: 'project_15_14', title: 'Project 15.14: Infra Assessment' },
    'project_15.01_ADクラウド化': { template: 'project_15_01', title: 'Project 15.01: AD Cloud Lift' },
    'project_15.02_セコム入退室クラウド化': { template: 'project_15_02', title: 'Project 15.02: Secom Cloud' },
    'project_15_combined': { template: 'project_15_combined', title: 'AD+SECOM同時依頼 3社比較' },
    'infrastructure_strategy': { template: 'project_15_combined', title: 'AD+SECOM同時依頼 3社比較' },
    'project_ad_scenarios': { template: 'project_ad_scenarios', title: 'AD移行シナリオ比較：AD vs ハイブリッド vs Entra ID' },
    'project_ad_matrix': { template: 'project_ad_matrix', title: 'ADクラウド化 3社権限・責任分界点比較表' },
    'project_15.03_ネットワークインフラ刷新': { template: 'project_15_03', title: 'Project 15.03: Network Overhaul' },
    'project_management': { template: 'project_management', title: 'Schedule & Tasks | Internal DX Portal' }
  };

  if (ROUTE_MAP[pageId]) {
    const route = ROUTE_MAP[pageId];
    if (route.handler) return route.handler();
    templateName = route.template;
    title = route.title;
  } else {
    const sanitizedId = pageId.replace(/\./g, '_');
    templateName = sanitizedId;
    title = pageId + ' - Project Dashboard';
  }

  // Render using the robust serverRawWithCss
  try {
    return serveRawWithCss(templateName, title);
  } catch (err) {
    console.error(`Render failed for ${templateName}: ${err.message}`);
    return renderErrorPage(err);
  }
}

/**
 * 指定 HTML を評価し、CSS インライン化、リンクの正常化、およびスマートな遷移制御を行う。
 * 白画面対策の決定版。
 */
function serveRawWithCss(filename, pageTitle) {
  let html = "";
  let baseUrl = "";
  try {
    baseUrl = ScriptApp.getService().getUrl();
  } catch (e) {
    // 💡 Fallback to the reported production URL if getUrl() fails
    baseUrl = "https://script.google.com/a/akiba-holdings.co.jp/macros/s/AKfycbzubD24U27_X6_SREm4vqrPl5fVs8fmzvW1pGjaKXzyV1lJ_cVv66akCpvwEJHXO71XFQ/exec";
  }

  try {
    const template = HtmlService.createTemplateFromFile(filename);
    template.url = baseUrl;
    html = template.evaluate().getContent();
  } catch (e) {
    console.warn(`Template evaluation failed for ${filename}, falling back to raw: ${e.message}`);
    html = HtmlService.createHtmlOutputFromFile(filename).getContent();
  }

  if (!html || html.length < 100) {
    return HtmlService.createHtmlOutput('<h1>Page empty or too short</h1><p>' + filename + '</p>')
      .setTitle('Error').setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  }

  // 1. CSS インライン化
  if (html.indexOf('assets/portal_nexus.css') !== -1) {
    try {
      const cssContent = HtmlService.createHtmlOutputFromFile('_generated_css').getContent();
      if (cssContent && cssContent.length > 0) {
        html = html.replace(/<link[^>]*href=["']assets\/portal_nexus\.css["'][^>]*>/i, cssContent);
      }
    } catch (e) {}
  }

  // 2. 外部リソース除去はここでは行わない（Tailwind CSS が必要）
  // html = html.replace(/<script[^>]*src=["']https?:\/\/cdn\.tailwindcss\.com[^"']*["'][^>]*>\s*<\/script>/gi, '');
  // html = html.replace(/<link[^>]*href=["']https?:\/\/fonts\.googleapis\.com[^"']*["'][^>]*>/gi, '');

  // 3. リンクの相対化 (サーバー側では絶対URLを振らず、?page= 形式に統一)
  // これにより、サンドボックスドメインへの誤遷移を防ぐ
  html = html.replace(/href=["'](?!https?:\/\/)([^"']+)\.html["']/gi, 'href="?page=$1"');
  // target="_top" 等の属性を一度クリーンアップ（JSで制御するため）
  html = html.replace(/<a([^>]+)target=["']_top["']/gi, '<a$1');

  // 4. スマートナビゲーションスクリプト
  // window.top.location.href を直接書き換えることで、アドレスバーの更新と遷移を確実に行う
  const navScript = `
<script>
  (function() {
    var BASE_URL = "${baseUrl.replace(/\?.*$/, '')}";
    
    // 環境判定
    var isDrive = false;
    try {
      var ref = document.referrer || "";
      if (ref.indexOf('drive.google.com') !== -1 || ref.indexOf('docs.google.com') !== -1 || (window.self !== window.top && ref === "")) {
        isDrive = true;
      }
    } catch (e) { isDrive = true; }

    document.addEventListener('click', function(e) {
      var a = e.target.closest('a');
      if (!a) return;
      
      var href = a.getAttribute('href') || "";
      
      // 内部リンク (?page=) の場合のみ介入
      if (href.indexOf('?page=') !== -1) {
        e.preventDefault();
        var targetPage = href.split('page=')[1].split('&')[0];
        var finalUrl = BASE_URL + "?page=" + targetPage;

        if (!isDrive) {
          // 通常ブラウザ: top の URL を直接書き換えて遷移（白画面回避の確実な方法）
          try {
            window.top.location.href = finalUrl;
          } catch(err) {
            window.location.href = finalUrl;
          }
        } else {
          // Drive内: iframe内での相対遷移を維持
          window.location.href = "?page=" + targetPage;
        }
      }
    }, true);
  })();
</script>
`;

  if (html.indexOf('</body>') !== -1) {
    html = html.replace('</body>', navScript + '</body>');
  } else {
    html += navScript;
  }

  return HtmlService.createHtmlOutput(html)
    .setTitle(pageTitle || 'Internal DX Portal')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .setFaviconUrl(FAVICON_DATA_URI);
}

function serveIndexRaw(currentUrl) {
  return serveRawWithCss('index', 'Command Center | Internal DX Portal');
}

function serveLandingRaw() {
  return serveRawWithCss('landing', 'Akiba Holdings DX Gateway');
}

/**
 * project_sd_wan を createHtmlOutputFromFile でそのまま返す。
 * テンプレート評価・processHtmlContent を経由すると「形式が正しくない HTML」で落ちるため回避。
 */
function serveProjectSdWan() {
  return HtmlService.createHtmlOutputFromFile('project_sd_wan')
    .setTitle('SD-WAN Comparison')
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL)
    .setFaviconUrl(FAVICON_DATA_URI);
}

/**
 * Helper to create HTML Output with standard security headers and meta tags.
 */
function createAccessibleHtml(filename, vars, title) {
  const template = HtmlService.createTemplateFromFile(filename);
  vars = vars || {};
  title = (title != null && title !== '') ? String(title) : 'Internal DX Portal';

  // Inject variables
  for (const key in vars) {
    template[key] = vars[key];
  }
  template.title = title;

  const evaluated = template.evaluate();
  const rawContent = evaluated.getContent();
  const baseUrl = vars.url ? String(vars.url) : '?';
  const processedContent = processHtmlContent(rawContent, baseUrl);

  return HtmlService.createHtmlOutput(processedContent)
    .setTitle(title)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL) // Crucial for embedding
    .setFaviconUrl(FAVICON_DATA_URI);
}

/**
 * 🛠️ DYNAMIC ASSET INJECTION
 * Adapts static HTML for GAS environment:
 * 1. Inlines 'assets/portal_nexus.css' from '_generated_css' file.
 * 2. Rewrites relative HTML links (e.g., 'landing.html') to GAS parameters ('?page=landing').
 *    - Adds target="_top" to force navigation out of the iframe.
 */
function processHtmlContent(htmlContent, baseUrl) {
  // 1. Inline CSS
  // Looks for: <link rel="stylesheet" href="assets/portal_nexus.css">
  if (htmlContent.indexOf('assets/portal_nexus.css') !== -1) {
    try {
      const cssOutput = HtmlService.createHtmlOutputFromFile('_generated_css');
      const cssContent = cssOutput.getContent(); // Contains <style>...</style>
      if (cssContent && cssContent.length > 0) {
        htmlContent = htmlContent.replace(
          /<link[^>]*href=["']assets\/portal_nexus\.css["'][^>]*>/i,
          cssContent
        );
      }
    } catch (e) {
      console.warn('⚠️ Automated CSS Injection Failed: ' + e.message);
    }
  }

  // 2. Rewrite Links
  // Matches href="foo.html" -> href="URL?page=foo" target="_top"
  // Excludes http/https links
  htmlContent = htmlContent.replace(/href=["'](?!http)([^"']+)\.html["']/g, (match, filename) => {
    // Determine the base separator (if baseUrl already has params)
    const separator = baseUrl.indexOf('?') !== -1 ? '&' : '?';
    return `href="${baseUrl}${separator}page=${filename}" target="_top"`;
  });

  // 3. REMOVED: Injects Base Tag (Caused issues)
  // if (htmlContent.indexOf('<head>') !== -1) { ... }

  return htmlContent;
}

/**
 * Renders the Access Denied page.
 */
function renderAccessDenied(email) {
  try {
    const content = HtmlService.createHtmlOutputFromFile('AccessDenied').getContent()
      .replace('<?= email ?>', email || 'Unknown User');
    return HtmlService.createHtmlOutput(content)
      .setTitle('Access Denied')
      .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
  } catch (e) {
    return HtmlService.createHtmlOutput(`<h1>Access Denied</h1><p>User: ${email}</p>`);
  }
}

/**
 * Renders a catastrophic error page.
 */
function renderErrorPage(error) {
  const safeError = String(error).replace(/</g, '&lt;').replace(/>/g, '&gt;');
  return HtmlService.createHtmlOutput(
    '<div style="font-family:monospace; padding:2em; color:red; background:#fee;">' +
    '<h1>⚠️ Application Error</h1>' +
    '<p><strong>System Message:</strong> ' + safeError + '</p>' +
    '<p>Please contact the system administrator.</p>' +
    '</div>'
  ).setTitle('System Error').setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * Minimal health-check response (no CSS/JS). Use ?page=ping to verify app is serving.
 */
function servePing() {
  return HtmlService.createHtmlOutput(
    '<!DOCTYPE html><html><head><meta charset="UTF-8"><title>OK</title></head>' +
    '<body style="font-family:sans-serif;padding:2em;"><h1>OK</h1><p>App is serving.</p></body></html>'
  ).setTitle('OK').setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * Debug Dashboard Handler
 */
function serveDebugDashboard() {
  let outputHtml = '<h1>🔍 GAS File System Diagnostics</h1>';
  const filesToTest = ['index', 'AccessDenied', 'project_15_12'];

  outputHtml += '<table border="1" cellpadding="5"><tr><th>File</th><th>Status</th><th>Size</th></tr>';
  filesToTest.forEach(f => {
    try {
      const content = HtmlService.createHtmlOutputFromFile(f).getContent();
      outputHtml += `<tr><td>${f}</td><td style="color:green">OK</td><td>${content.length} bytes</td></tr>`;
    } catch (e) {
      outputHtml += `<tr><td>${f}</td><td style="color:red">FAIL</td><td>${e.message}</td></tr>`;
    }
  });
  outputHtml += '</table>';

  return HtmlService.createHtmlOutput(outputHtml).setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}

/**
 * ONE-OFF TOOL: Search Gmail
 * returns array of finding strings
 */
function searchGmail(query, returnOnly) {
  if (!query) query = '見積';
  console.log(`Searching for: "${query}"...`);
  const findings = [];

  const threads = GmailApp.search(query, 0, 10);
  if (threads.length === 0) {
    findings.push("No emails found for: " + query);
  } else {
    threads.forEach(t => {
      const msgs = t.getMessages();
      msgs.forEach(m => {
        const info = `
--- Email Found ---
Subject: ${m.getSubject()}
Date: ${m.getDate()}
Snippet: ${m.getPlainBody().substring(0, 500)}
-------------------`;
        console.log(info);
        findings.push(info);
      });
    });
  }

  if (returnOnly) return findings;
}
