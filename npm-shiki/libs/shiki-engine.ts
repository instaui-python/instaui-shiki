import { createOnigurumaEngine } from "shiki/engine/oniguruma";
import getWasm from "shiki/wasm";
import { getAppInfo } from "instaui";

const appInfo = getAppInfo();

if (!appInfo || appInfo.mode === "zero") {
  (window as any)["__shiki_engine_wasm__"] = createOnigurumaEngine(getWasm);
}

export function getEngine() {
  return createOnigurumaEngine(getWasm);
}
