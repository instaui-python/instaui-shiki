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
        "shiki-code": path.resolve(__dirname, "libs/main.ts"),
        "shiki-engine": path.resolve(__dirname, "libs/shiki-engine.ts"),
        "shiki-code-logic": path.resolve(__dirname, "libs/shiki-code-logic.ts"),
        "shiki-transformers": path.resolve(
          __dirname,
          "libs/shiki-transformers.ts"
        ),
      },
      fileName: (_, entryName) => `${entryName}.js`,
      formats: ["es"],
      cssFileName: "shiki-style",
    },
    // sourcemap: true,

    rollupOptions: {
      external: [
        "vue",
        "@/shiki-code-logic",
        "@shiki/transformers",
        "instaui",
        "shiki-engine",
      ],
    },
  },
});
