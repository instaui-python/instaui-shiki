<script setup lang="ts">
import {
  h,
  ref,
  watch,
  computed,
  normalizeClass as _normalizeClass,
} from "vue";
import type { TProps } from "./types";
import {
  highlighterTask,
  getTransformers,
  readyCopyButton,
} from "./shiki_code";

const props = defineProps<TProps>();

const {
  transformers: transformerNames = [],
  themes = {
    light: "vitesse-light",
    dark: "vitesse-dark",
  },
} = props;

const highlightedCode = ref("");
const realLanguage = computed(() => props.language || "python");
const realTheme = computed(() => props.theme || "light");
const realLineNumbers = computed(() => props.lineNumbers ?? true);
const classes = computed(() => {
  return _normalizeClass([
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
    code = code.trim();
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
    });
  },
  { immediate: true }
);

// copy button
const { copyButtonClick, btnClasses } = readyCopyButton(props);
</script>

<template>
  <div :class="classes">
    <button
      :class="btnClasses"
      title="Copy Code"
      @click="copyButtonClick"
    ></button>
    <span class="lang">{{ realLanguage }}</span>
    <div v-html="highlightedCode" style="overflow: hidden"></div>
  </div>
</template>

<style scoped></style>
