import type { Ref } from "vue";

export type TProps = {
  code: string;
  language: string;
  theme?: string;
  themes: Record<string, string>;
  transformers: string[];
  lineNumbers: boolean;
  useDarkRef: Ref<boolean>;
  decorations: Record<string, any>[];
};
