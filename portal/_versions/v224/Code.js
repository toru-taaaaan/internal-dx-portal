// 🚀 GAS Expert: Robust & Scalable Backend
// 3D Brain Icon from IconArchive
const FAVICON_DATA_URI = 'https://icons.iconarchive.com/icons/microsoft/fluentui-emoji-3d/96/Brain-3d-icon.png';

// 🛡️ SECURITY CONFIGURATION
// 🛡️ SECURITY CONFIGURATION
const CONFIG = {
  ADMIN_EMAILS: ['tanji@akiba-holdings.co.jp', 'shino@akiba-holdings.co.jp'],
  GUEST_USERS: [
    'nakano@akiba-holdings.co.jp', 
    'yudai.ishii@adtec.co.jp', 
    'ishii@akiba-holdings.co.jp'
  ],
  ALLOWED_GROUP: '', // Disabled for strict control
  DEBUG_BYPASS_AUTH: true // 🔓 TEMPORARILY DISABLED FOR TESTING
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
  let isDynamic = false;

  // Basic Routing Map
  const ROUTE_MAP = {
    'home': { template: 'index', title: 'Internal DX Portal - Command Center' },
    'landing': { template: 'landing', title: 'Akiba Holdings DX Gateway' },
    'debug': { handler: serveDebugDashboard },
    'project_15_12_ishii': { template: 'project_15_12_ishii', title: '石井様向け相談資料' },
    'project_15_12_proposal': { template: 'project_15_12_proposal', title: 'AquaVoice提案書' },
    'project_15_12_antigravity': { template: 'project_15_12_antigravity', title: 'Antigravity導入案内' },
    'project_buddynet': { template: 'project_buddynet', title: 'BuddyNet DX Portal' },
    'project_sd_wan': { template: 'project_sd_wan', title: 'SD-WAN Comparison' },
    'project_15.12_AIチャンピオン推進': { template: 'project_15_12', title: 'Project 15.12: AI Champion Portal' },
    // Legacy Routes (Japanese Params)
    'project_15.14_現状インフラ評価': { template: 'project_15_14', title: 'Project 15.14: Infra Assessment' },
    'project_15.01_ADクラウド化': { template: 'project_15_01', title: 'Project 15.01: AD Cloud Lift' },
    'project_15.02_セコム入退室クラウド化': { template: 'project_15_02', title: 'Project 15.02: Secom Cloud' },
    'project_15_combined': { template: 'project_15_combined', title: 'AD+SECOM同時依頼 3社比較' },
    'project_15.03_ネットワークインフラ刷新': { template: 'project_15_03', title: 'Project 15.03: Network Overhaul' }
  };

  // 1. Check Explicit Routes
  if (ROUTE_MAP[pageId]) {
    const route = ROUTE_MAP[pageId];
    if (route.handler) return route.handler();
    templateName = route.template;
    title = route.title;
  } 
  // 2. Dynamic Project Routing (Low code fallback)
  else if (pageId.indexOf('15.') !== -1 || pageId.indexOf('project_') !== -1) {
    templateName = pageId; // Try to load file with same name
    title = pageId + ' - Project Dashboard';
    isDynamic = true;
  }

  // 3. Render
  try {
    return createAccessibleHtml(templateName, { 
      url: currentUrl, 
      projectId: pageId 
    }, title);
  } catch (renderErr) {
    console.warn(`Template '${templateName}' not found. Falling back to generic project template.`);
    return createAccessibleHtml('project', {
      url: currentUrl,
      projectId: pageId,
      error: "Requested specific dashboard not found, showing generic view."
    }, 'Project Details');
  }
}

/**
 * Helper to create HTML Output with standard security headers and meta tags.
 */
function createAccessibleHtml(filename, vars, title) {
  const template = HtmlService.createTemplateFromFile(filename);
  
  // Inject variables
  if (vars) {
    for (const key in vars) {
      template[key] = vars[key];
    }
  }

  return template.evaluate()
    .setTitle(title)
    .addMetaTag('viewport', 'width=device-width, initial-scale=1')
    .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL) // Crucial for embedding
    .setFaviconUrl(FAVICON_DATA_URI);
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
  return HtmlService.createHtmlOutput(
    `<div style="font-family:monospace; padding:2em; color:red; background:#fee;">
      <h1>⚠️ Application Error</h1>
      <p><strong>System Message:</strong> ${error.toString()}</p>
      <p>Please contact the system administrator.</p>
    </div>`
  ).setTitle('System Error').setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
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
 