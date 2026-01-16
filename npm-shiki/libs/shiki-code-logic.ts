import { computed, normalizeClass, watch } from "vue";
import { useClipboard } from "@vueuse/core";
import { createHighlighter } from "@/shiki-core";
import type { TProps } from "@/types";

export const highlighterTask = createHighlighter({
  themes: ["vitesse-dark", "vitesse-light"],
});

function transformersModuleGetter() {
  let module: any = null;

  return async () => {
    if (!module) {
      // @ts-ignore
      module = await import(`@shiki/transformers`);
    }
    return module;
  };
}

export const getTransformersModule = transformersModuleGetter();

export async function getTransformers(names: string[]) {
  if (names.length === 0) {
    return [];
  }

  const tfModule: any = await getTransformersModule();
  return names.map((name) => {
    const realName = `transformer${
      name.charAt(0).toUpperCase() + name.slice(1)
    }`;
    return tfModule[realName]();
  });
}

export function readyCopyButton(props: TProps) {
  const { copy, copied } = useClipboard({ source: props.code, legacy: true });

  const btnClasses = computed(() => {
    return normalizeClass(["copy", { copied: copied.value }]);
  });

  /**
   *
   * @param {Event} e
   */
  function copyButtonClick(e: Event) {
    copy(props.code);

    watch(
      copied,
      (copied) => {
        if (!copied) {
          (e.target! as any).blur();
        }
      },
      { once: true }
    );
  }

  return {
    copyButtonClick,
    btnClasses,
  };
}
