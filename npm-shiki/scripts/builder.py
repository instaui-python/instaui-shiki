from pathlib import Path
import shutil

PORJECT_ROOT = Path(__file__).parent.parent.resolve()

SHIKE_LANGS_NODE_MODULES = PORJECT_ROOT.joinpath(
    "node_modules/.pnpm/@shikijs+langs@3.7.0/node_modules/@shikijs/langs/dist"
).resolve()

SHIKE_THEMES_NODE_MODULES = PORJECT_ROOT.joinpath(
    "node_modules/.pnpm/@shikijs+themes@3.7.0/node_modules/@shikijs/themes/dist"
).resolve()

PY_ROOT = PORJECT_ROOT.parent

DIST_PATH = PORJECT_ROOT.joinpath("dist").resolve()


SHIKI_CODE_FILE = DIST_PATH.joinpath("shiki_code.js").resolve()
SHIKI_TRANSFORMERS_FILE = DIST_PATH.joinpath("shiki-transformers.js").resolve()
SHIKI_STYLE_FILE = DIST_PATH.joinpath("shiki-style.css").resolve()

STATIC_PATH = PY_ROOT.joinpath("src/instaui_shiki/static").resolve()


LANGS_FILES = [
    "css.mjs",
    "markdown.mjs",
    "python.mjs",
    "shell.mjs",
    "shellscript.mjs",
]
THEMES_FILES = [
    "vitesse-dark.mjs",
    "vitesse-light.mjs",
]


def copy_shiki_files():
    langs_dir = SHIKE_LANGS_NODE_MODULES
    themes_dir = SHIKE_THEMES_NODE_MODULES

    langs_dest = STATIC_PATH.joinpath("langs")
    themes_dest = STATIC_PATH.joinpath("themes")

    # 确保 langs 和 themes 目录
    langs_dest.mkdir(parents=True, exist_ok=True)
    themes_dest.mkdir(parents=True, exist_ok=True)

    # 按 LANGS_FILES 和 THEMES_FILES 复制文件到 langs 和 themes 目录
    for fname in LANGS_FILES:
        src = langs_dir / fname
        dst = langs_dest / fname
        shutil.copyfile(src, dst)  # 复制并保留元数据

    for fname in THEMES_FILES:
        src = themes_dir / fname
        dst = themes_dest / fname
        shutil.copyfile(src, dst)


def copy_to_static():
    shutil.copyfile(SHIKI_CODE_FILE, STATIC_PATH.joinpath(SHIKI_CODE_FILE.name))
    shutil.copyfile(
        SHIKI_TRANSFORMERS_FILE, STATIC_PATH.joinpath(SHIKI_TRANSFORMERS_FILE.name)
    )
    shutil.copyfile(SHIKI_STYLE_FILE, STATIC_PATH.joinpath(SHIKI_STYLE_FILE.name))


def copy2py():
    # 清除 static 目录
    shutil.rmtree(STATIC_PATH, ignore_errors=True)
    STATIC_PATH.mkdir(parents=True, exist_ok=True)

    copy_shiki_files()
    copy_to_static()
    print(f"Copied to static folder [{STATIC_PATH}]")


if __name__ == "__main__":
    # show_all_paths()
    copy2py()
