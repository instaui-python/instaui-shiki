import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  base: "./",

  build: {
    lib: {
      entry: {
        shiki_code: path.resolve(__dirname, "libs/main.ts"),
        "shiki-transformers": path.resolve(
          __dirname,
          "libs/shiki_transformers.ts"
        ),
      },
      fileName: (_, entryName) => `${entryName}.js`,
      formats: ["es"],
      cssFileName: "shiki-style",
    },
    // sourcemap: true,

    rollupOptions: {
      external: ["vue", "@shiki/transformers"],
    },
  },
});
