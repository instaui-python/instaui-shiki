import type { Ref } from "vue";

declare module "instaui" {
  export function useBindingGetter(): {
    getRef: (key: any) => Ref;
  };

  export function useLanguage(): Ref<string>;
}
