__all__ = [
    "recursively_import_packages",
]

import os
import importlib
import traceback
from pathlib import Path
from glob import glob


def recursively_import_packages(
        entry_package: str,
        fail_continue: bool = True):
    """
    递归倒入一个包以及包含的模块和包
    :param entry_package: 入口包名
    :param fail_continue: 如果任何一个模块导入失败，是否继续导入下一个
    """
    entry_module = importlib.import_module(entry_package)
    entry = entry_module.__file__
    if not Path(entry).is_dir() and not entry.endswith("__init__.py"):
        # 如果给定的entry_module不是一个目录且也不是包的init文件，
        # 则视为需要导入的仅仅是该包本身，无需递归循环
        return
    if entry.endswith("__init__.py"):
        entry = Path(entry).parent
    entry = str(entry)
    prefix = os.sep.join(entry.split(os.sep)[:-len(entry_package.split("."))])
    module_dirs = [
        *glob(
            str(Path(entry) / "**.py"),
            recursive=True
        ),
        *glob(
            str(Path(entry) / f"**{os.sep}**.py"),
            recursive=True
        )
    ]
    for module_dir in module_dirs:
        cut_path_without_ext, _ = os.path.splitext(module_dir[len(prefix):])
        if "-" in cut_path_without_ext or " " in cut_path_without_ext:
            continue
        package_name_to_import = ".".join([i for i in cut_path_without_ext.split(os.sep) if i and i.strip()])
        try:
            exec(f"import {package_name_to_import}")
        except Exception as e:
            print(f"!!!FAILED TO IMPORT {package_name_to_import}!!!: {e}")
            print(traceback.format_exc())
            if not fail_continue:
                raise e
