// 🚀 GAS Expert: Robust & Scalable Backend
// 3D Brain Icon from IconArchive
const FAVICON_DATA_URI = 'https://icons.iconarchive.com/icons/microsoft/fluentui-emoji-3d/96/Brain-3d-icon.png';

// 🛡️ SECURITY CONFIGURATION
const CONFIG = {
  ALLOWED_EMAILS: ['tanji@akiba-holdings.co.jp'],
  ALLOWED_GROUP: 'system@akiba-holdings.co.jp',
  DEBUG_BYPASS_AUTH: true // Set to false in production
};

/**
 * Main Entry Point (GET Request)
 */
function doGet(e) {
  // Global Safety Net
  try {
    const userEmail = Session.getActiveUser().getEmail();
    
    // 1. Authorization
    if (!isUserAuthorized(userEmail)) {
      return renderAccessDenied(userEmail);
    }

    // 2. Routing
    const pageId = e.parameter.page || 'home';
    return resolveRoute(pageId, ScriptApp.getService().getUrl());

  } catch (criticalErr) {
    console.error('Critical Failure: ' + criticalErr);
    return renderErrorPage(criticalErr);
  }
}

/**
 * Checks if the current user is allowed to access the portal.
 */
function isUserAuthorized(email) {
  if (CONFIG.DEBUG_BYPASS_AUTH) return true;
  if (CONFIG.ALLOWED_EMAILS.indexOf(email) !== -1) return true;
  
  if (CONFIG.ALLOWED_GROUP && email) {
    try {
      if (GroupsApp.getGroupByEmail(CONFIG.ALLOWED_GROUP).hasUser(email)) return true;
    } catch (e) {
      console.warn('Group check error: ' + e);
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
    'debug': { handler: serveDebugDashboard },
    'project_15_12_ishii': { template: 'project_15_12_ishii', title: '石井様向け相談資料' },
    'project_15_12_proposal': { template: 'project_15_12_proposal', title: 'AquaVoice提案書' },
    'project_15_12_antigravity': { template: 'project_15_12_antigravity', title: 'Antigravity導入案内' },
    'project_buddynet': { template: 'project_buddynet', title: 'BuddyNet DX Portal' },
    'project_sd_wan': { template: 'project_sd_wan', title: 'SD-WAN Comparison' },
    'project_15.12_AIチャンピオン推進': { template: 'project_15_12', title: 'Project 15.12: AI Champion Portal' }
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
