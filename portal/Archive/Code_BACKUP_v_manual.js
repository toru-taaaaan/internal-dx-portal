// ULTRA MINIMAL CODE.JS - EMERGENCY RESTORE
function doGet(e) {
    return HtmlService.createHtmlOutput('<h1>ALIVE</h1><p>If you see this, GAS is working.</p>')
        .setXFrameOptionsMode(HtmlService.XFrameOptionsMode.ALLOWALL);
}
