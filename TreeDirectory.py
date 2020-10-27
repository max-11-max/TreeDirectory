import argparse
from pathlib import Path, PurePath, PureWindowsPath
import os
from typing import List

"""features:
Include system files
Open file (if exists)
Rename file (if exists)
Tree display
Multiple drives
Choose which directory to start from
Open files

"""

parser = argparse.ArgumentParser(description='File Directory: automatically '
                                             'starts from current drive and '
                                             'user')
parser.add_argument('-t', '--tree', help='Return Tree of Directory',
                    action='store_true')
parser.add_argument('-s', '--system_files',
                    help='sets --tree to include system files as well',
                    action='store_true')
parser.add_argument('-o', '--open', type=str, metavar='', help='Open given file')

args = parser.parse_args()


def tree(home_path: str):
    print(PurePath(home_path).parts[-1])
    if Path(home_path).is_dir():
        for child in os.listdir(home_path):
            branches(home + '\\' + child, [])
    else:
        return


def branches(file: str, branch: List[str]) -> None:
    try:
        Path(file).is_dir() and Path(file).is_file
    except OSError:
        return
    else:
        print(''.join(branch) + '|__' + PurePath(file).parts[-1])
        if Path(file).is_dir():
            try:
                os.listdir(file)
            except PermissionError:
                return
            else:
                if len(os.listdir(file)) > 100:
                    return
                else:
                    for child in os.listdir(file): #seems to be screwing it up
                        if Path(file).parts[-1] == os.listdir(PurePath(file).parent)[-1]:
                            branches(file + '\\' + str(child), branch + ['  '])
                        else:
                            branches(file + '\\' + str(child), branch + ['| '])
        else:
            return


"""def print_branches(path: str, prefix: List[str]):
    try:
        Path(path).is_dir() and Path(path).is_file()
    except OSError:
        return
    else:
        try:

            os.listdir(path)
        except PermissionError:
            return
        else:
"""



if __name__ == '__main__':
    if args.tree:
        if args.system_files:
            home = Path.home().parts[0]
            tree(home)
        else:
            home = ''
            for part in Path.home().parts:
                if part[-2:] == '\\':
                    home += part
                else:
                    home = home + part + '\\'
            tree(home)

