export type TProps = {
  code: string;
  language: string;
  theme?: string;
  themes: Record<string, string>;
  transformers: string[];
  lineNumbers: boolean;
  useDark: boolean;
  decorations: Record<string, any>[];
};
