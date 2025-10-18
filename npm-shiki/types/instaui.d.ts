import type { Ref } from "vue";

declare module "instaui" {
  export function useBindingGetter(): {
    getValue: (key: any) => any;
  };

  export function useLanguage(): Ref<string>;
}
