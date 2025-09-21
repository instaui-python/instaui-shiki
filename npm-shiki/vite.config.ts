import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import path from "path";

// https://vite.dev/config/
export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      "@": path.resolve(__dirname, "libs"),
    },
  },
  base: "./",

  build: {
    lib: {
      entry: {
        shiki_code: path.resolve(__dirname, "libs/main.ts"),
        shiki_code_logic: path.resolve(__dirname, "libs/shiki_code_logic.ts"),
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
      external: ["vue", "@/shiki_code_logic", "@shiki/transformers", "instaui"],
    },
  },
});
