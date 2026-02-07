// 3D Brain Icon from IconArchive (Microsoft Fluent 3D) - Robust URL
const FAVICON_DATA_URI = 'https://icons.iconarchive.com/icons/microsoft/fluentui-emoji-3d/96/Brain-3d-icon.png';

function doGet(e) {
    var output;
    try {
        var page = e.parameter.page;
        var template;

        if (!page) {
            // Index page
            template = HtmlService.createTemplateFromFile('index');
            template.title = 'Internal DX Portal';
        } else if (page.indexOf('15.') !== -1) {
            // Dynamic routing for 15.xx projects
            var match = page.match(/15\.(\d+)/);
            if (match) {
                var subId = match[1];
                var templateName = 'project_15_' + subId;
                try {
                    template = HtmlService.createTemplateFromFile(templateName);
                    template.title = page + ' - Project Dashboard';
                } catch (err) {
                    console.log('Template not found: ' + templateName);
                    template = HtmlService.createTemplateFromFile('project'); // Fallback
                    template.title = 'Project Details';
                    template.projectId = page;
                }
            } else {
                template = HtmlService.createTemplateFromFile('project');
                template.title = 'Project Details';
                template.projectId = page;
            }
        } else {
            // Generic fallback
            template = HtmlService.createTemplateFromFile('project');
            template.title = page.replace('project_', '');
            template.projectId = page;
        }

        output = template.evaluate()
            .setTitle(template.title)
            .addMetaTag('viewport', 'width=device-width, initial-scale=1');

    } catch (e) {
        return HtmlService.createHtmlOutput('Error: ' + e.toString());
    }

    // --- ROBUST FAVICON SETTING ---
    // Apply favicon in a separate try-catch block so it never crashes the app
    try {
        output.setFaviconUrl(FAVICON_DATA_URI);
    } catch (iconError) {
        console.error('Favicon failed to load: ' + iconError);
        // Silently fail or set a default if needed, but do not crash.
    }

    return output;
}
