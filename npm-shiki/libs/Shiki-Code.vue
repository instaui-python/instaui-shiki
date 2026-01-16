<script setup lang="ts">
import { ref, watch, computed, normalizeClass } from "vue";
import { useBindingGetter, useLanguage } from "instaui";
import type { TProps } from "@/types";
import {
  highlighterTask,
  getTransformers,
  readyCopyButton,
} from "@/shiki-code-logic";
import { trimNewlines } from "./utils";

const props = defineProps<TProps>();

const {
  transformers: transformerNames = [],
  themes = {
    light: "vitesse-light",
    dark: "vitesse-dark",
  },
  useDark,
} = props;
const { getRef } = useBindingGetter();
const dark = getRef(useDark);
const highlightedCode = ref("");
const realLanguage = computed(() => props.language || "python");
const realTheme = computed(
  () => props.theme || (dark.value ? "dark" : "light")
);
const realLineNumbers = computed(() => props.lineNumbers ?? true);
const classes = computed(() => {
  return normalizeClass([
    `language-${realLanguage.value}`,
    `theme-${realTheme.value}`,
    `shiki-code`,
    { "line-numbers": realLineNumbers.value },
  ]);
});

watch(
  [() => props.code, realTheme],
  async ([code, _]) => {
    if (!code) {
      return;
    }
    code = trimNewlines(code);
    const highlighter = await highlighterTask;
    const transformers = await getTransformers(transformerNames);

    highlightedCode.value = await highlighter.codeToHtml(code, {
      themes,
      lang: realLanguage.value,
      transformers,
      defaultColor: realTheme.value,
      colorReplacements: {
        "#ffffff": "#f8f8f2",
      },
      decorations: props.decorations,
    });
  },
  { immediate: true }
);

// copy button
const { copyButtonClick, btnClasses } = readyCopyButton(props);

const language = useLanguage();

const style = computed(() => {
  return `--shiki-code-copy-copied-text-content: '${
    language.value === "zh_CN" ? "已复制" : "Copied"
  }'`;
});
</script>

<template>
  <div :class="classes" :style="style">
    <button
      :class="btnClasses"
      title="Copy Code"
      @click="copyButtonClick"
    ></button>
    <span class="lang">{{ realLanguage }}</span>
    <div v-html="highlightedCode" style="overflow: hidden"></div>
  </div>
</template>
