import { createHighlighterCore } from "shiki/core";
import { getAppInfo } from "instaui";

async function createHighlighter(options: {
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
      (theme) => import(/* @vite-ignore */ `${themeModulePath}${theme}.mjs`),
    ),
  );

  const appInfo = getAppInfo();

  const engine =
    !appInfo || appInfo.mode === "zero"
      ? (window as any)["__shiki_engine_wasm__"]
      : (await import("@/shiki-engine")).getEngine();

  const highlighter = await createHighlighterCore({
    themes: themesModule,
    engine: engine,
  });

  async function codeToHtml(code: string, options: any) {
    const { lang } = options;
    if (lang) {
      await highlighter.loadLanguage(
        import(/* @vite-ignore */ `${langModulePath}${lang}.mjs`),
      );
    }

    return highlighter.codeToHtml(code, options);
  }

  return {
    codeToHtml,
  };
}

let _highlighterPromise: ReturnType<typeof createHighlighter> | null = null;

export function getHighlighter() {
  if (!_highlighterPromise) {
    _highlighterPromise = createHighlighter({
      themes: ["vitesse-dark", "vitesse-light"],
    });
  }
  return _highlighterPromise;
}
