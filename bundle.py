import keyword
from typing import Dict, List, Tuple, Union
from pathlib import Path

VERSION = "5.15.4"
PKG_DIR = Path(__file__).parent / "fonticon_mdi5"


def get_data(version: str, pkg_dir: str) -> List[Tuple[Dict[str, str], str, str]]:
    """This function should return a list of OTF entries.

    Each entry is a 3-tuple:
        1. a charmap dict: {font label -> 4-letter unicode string}
        2. the name of the OTF file (should be placed in the font_dir)
        3. a name for the Enum class that will represent this OTF file.
    """
    font_dir = Path(pkg_dir) / "fonts"
    font_dir.mkdir(exist_ok=True)
    ...


def _normkey(key: str):
    if key[0].isdigit():
        key = "_" + key
    if keyword.iskeyword(key):
        key += "_"
    key = key.replace("-", "_")
    if not key.isidentifier():
        raise ValueError(f"not identifier: {key}")
    return key


TEMPLATE = """
from pathlib import Path
from enum import Enum


class {name}(Enum):
    @classmethod
    def _font_file(self) -> str:
        fonts = Path(__file__).parent / "fonts"
        return str(fonts / "{file}")
""".strip()


def build(data, version, pkg):
    init = f"__version__ = {version!r}\n\n"
    _all = []

    for charmap, otf, name in data:
        code = TEMPLATE.format(name=name, file=otf.name) + "\n\n"
        for key, glpyh in charmap.items():
            code += f"    {_normkey(key)} = '\\u{glpyh}'\n"

        dest = Path(pkg) / f"{name.lower()}.py"
        dest.write_text(code)
        print("writing", dest)

        init += f"from .{name.lower()} import {name}\n"
        _all.append(name)

    init = f"__all__ = {_all!r}\n" + init
    (Path(pkg) / f"__init__.py").write_text(init)
    print("writing __init__.py")


def main(version: str, root: Union[Path, str]):
    build(get_data(version, root), version, root)


if __name__ == "__main__":
    main(version=VERSION, root=PKG_DIR)
