function doGet() {
    return HtmlService.createHtmlOutputFromFile('index')
        .setTitle('Internal DX Portal')
        .addMetaTag('viewport', 'width=device-width, initial-scale=1');
}
