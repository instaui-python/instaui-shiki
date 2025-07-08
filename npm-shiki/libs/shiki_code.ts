import { useClipboard } from "@vueuse/core";
import { createHighlighter } from "./shiki_core";
import { computed, normalizeClass as _normalizeClass, watch } from "vue";

export const highlighterTask = createHighlighter({
  themes: ["vitesse-dark", "vitesse-light"],
});

function transformersModuleGetter() {
  let module = null;

  return async () => {
    if (!module) {
      // @ts-ignore
      module = await import(`@shiki/transformers`);
    }
    return module;
  };
}

export const getTransformersModule = transformersModuleGetter();

/**
 *
 * @param {string[]} names
 */
export async function getTransformers(names) {
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

export function readyCopyButton(props) {
  const { copy, copied } = useClipboard({ source: props.code, legacy: true });

  const btnClasses = computed(() => {
    return _normalizeClass(["copy", { copied: copied.value }]);
  });

  /**
   *
   * @param {Event} e
   */
  function copyButtonClick(e) {
    copy(props.code);

    watch(
      copied,
      (copied) => {
        if (!copied) {
          e.target.blur();
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
