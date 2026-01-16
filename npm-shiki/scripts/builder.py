from pathlib import Path
import shutil

PORJECT_ROOT = Path(__file__).parent.parent.resolve()

SHIKI_LANGS_NODE_MODULES = PORJECT_ROOT.joinpath(
    "node_modules/.pnpm/@shikijs+langs@3.7.0/node_modules/@shikijs/langs/dist"
).resolve()

SHIKI_THEMES_NODE_MODULES = PORJECT_ROOT.joinpath(
    "node_modules/.pnpm/@shikijs+themes@3.7.0/node_modules/@shikijs/themes/dist"
).resolve()


#
PY_PROJECT_ROOT = PORJECT_ROOT.parent
PY_SHIKI_DIST = PY_PROJECT_ROOT.joinpath("shiki-dist").resolve()
DIST_PATH = PORJECT_ROOT.joinpath("dist").resolve()


SHIKI_CODE_FILE = DIST_PATH.joinpath("shiki-code.js").resolve()
SHIKI_TRANSFORMERS_FILE = DIST_PATH.joinpath("shiki-transformers.js").resolve()
SHIKI_STYLE_FILE = DIST_PATH.joinpath("shiki-style.css").resolve()

SHIKI_CORE_LOGIC_FILE = DIST_PATH.joinpath("shiki-code-logic.js").resolve()

STATIC_PATH = PY_PROJECT_ROOT.joinpath("src/instaui_shiki/static").resolve()

# shiki-engine
SHIKI_ENGINE_FILE = DIST_PATH.joinpath("shiki-engine.js").resolve()

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
    langs_dir = SHIKI_LANGS_NODE_MODULES
    themes_dir = SHIKI_THEMES_NODE_MODULES

    langs_dest = STATIC_PATH.joinpath("langs")
    themes_dest = STATIC_PATH.joinpath("themes")

    langs_dest.mkdir(parents=True, exist_ok=True)
    themes_dest.mkdir(parents=True, exist_ok=True)

    #
    for fname in LANGS_FILES:
        src = langs_dir / fname
        dst = langs_dest / fname
        shutil.copyfile(src, dst)

    for fname in THEMES_FILES:
        src = themes_dir / fname
        dst = themes_dest / fname
        shutil.copyfile(src, dst)


def reset_folder(folder: Path, *, parents: bool = False, exist_ok: bool = False):
    shutil.rmtree(folder, ignore_errors=True)
    folder.mkdir(parents=parents, exist_ok=exist_ok)


def copy_to_static():
    shutil.copyfile(SHIKI_CODE_FILE, STATIC_PATH.joinpath(SHIKI_CODE_FILE.name))
    shutil.copyfile(
        SHIKI_TRANSFORMERS_FILE, STATIC_PATH.joinpath(SHIKI_TRANSFORMERS_FILE.name)
    )
    shutil.copyfile(SHIKI_STYLE_FILE, STATIC_PATH.joinpath(SHIKI_STYLE_FILE.name))

    shutil.copyfile(
        SHIKI_CORE_LOGIC_FILE, STATIC_PATH.joinpath(SHIKI_CORE_LOGIC_FILE.name)
    )
    shutil.copyfile(SHIKI_ENGINE_FILE, STATIC_PATH.joinpath(SHIKI_ENGINE_FILE.name))

    # for cdn
    reset_folder(PY_SHIKI_DIST, exist_ok=True)
    shutil.copyfile(
        SHIKI_CORE_LOGIC_FILE, PY_SHIKI_DIST.joinpath(SHIKI_CORE_LOGIC_FILE.name)
    )


def copy2py():
    reset_folder(STATIC_PATH, parents=True, exist_ok=True)

    copy_shiki_files()
    copy_to_static()
    print(f"Copied to static folder [{STATIC_PATH}]")


if __name__ == "__main__":
    # show_all_paths()
    copy2py()
