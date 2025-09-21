from typing import Optional
from instaui.zero.options import CdnResourceOption
from instaui_shiki import consts


def override(
    *,
    shiki_code_logic_js: Optional[str] = None,
) -> CdnResourceOption:
    if not shiki_code_logic_js:
        return default_override()

    return CdnResourceOption(
        import_maps={consts.SHIKI_CODE_LOGIC_IMPORT_NAME: shiki_code_logic_js},
    )


def default_override() -> CdnResourceOption:
    return override(
        shiki_code_logic_js=consts.SHIKI_CODE_LOGIC_CDN,
    )
