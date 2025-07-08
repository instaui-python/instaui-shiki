import { createHighlighterCore } from "shiki/core";
import { createOnigurumaEngine } from "shiki/engine/oniguruma";
import getWasm from "shiki/wasm";

export async function createHighlighter(options: {
  themes: string[];
  themeModulePath?: string;
  langModulePath?: string;
}) {
  const {
    themes,
    themeModulePath = "@shiki/themes/",
    langModulePath = "@shiki/langs/",
  } = options;

  const themesModule = await Promise.all(
    themes.map(
      (theme) => import(/* @vite-ignore */ `${themeModulePath}${theme}.mjs`)
    )
  );

  const highlighter = await createHighlighterCore({
    themes: themesModule,
    engine: createOnigurumaEngine(getWasm),
  });

  async function codeToHtml(code: string, options: any) {
    const { lang } = options;
    if (lang) {
      await highlighter.loadLanguage(
        import(/* @vite-ignore */ `${langModulePath}${lang}.mjs`)
      );
    }

    return highlighter.codeToHtml(code, options);
  }

  return {
    codeToHtml,
  };
}
