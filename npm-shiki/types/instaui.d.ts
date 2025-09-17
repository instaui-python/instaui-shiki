declare module "instaui" {
  export function useBindingGetter(): {
    getValue: (key: any) => any;
  };
}
