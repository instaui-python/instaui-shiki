import { getAppInfo } from "instaui";
import { createOnigurumaEngine } from "shiki/engine/oniguruma";
import getWasm from "shiki/wasm";

const appInfo = getAppInfo();

if (!appInfo || appInfo.mode === "zero") {
  (window as any)["__shiki_engine_wasm__"] = createOnigurumaEngine(getWasm);
}

export function getEngine() {
  return createOnigurumaEngine(getWasm);
}
