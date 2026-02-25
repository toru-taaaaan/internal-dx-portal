const markdownItAttrs = require("markdown-it-attrs");

module.exports = function (eleventyConfig) {
  // 既存HTMLファイルはテンプレート処理せず、そのまま _site/ にコピー
  eleventyConfig.addPassthroughCopy({ "src/*.html": "." });

  // src/pages/ をそのまま _site/pages/ にコピー
  eleventyConfig.addPassthroughCopy("src/pages");

  // assets/ をそのままコピー
  eleventyConfig.addPassthroughCopy("assets");

  // src/images/ をコピー
  eleventyConfig.addPassthroughCopy({ "src/images": "images" });

  // Markdown設定: markdown-it-attrs でクラス付与を可能にする
  eleventyConfig.amendLibrary("md", (mdLib) => {
    mdLib.use(markdownItAttrs);
  });

  return {
    dir: {
      input: "src",
      output: "_site",
      includes: "_includes",
      data: "_data",
    },
    templateFormats: ["md", "njk"],
    markdownTemplateEngine: "njk",
  };
};
