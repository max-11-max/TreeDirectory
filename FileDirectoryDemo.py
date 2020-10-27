from pathlib import Path, PurePath, PureWindowsPath
import os
print(os.environ)
print(os.getlogin())
print(Path.home().parts)
print(os.listdir(Path.home().parts[0] + Path.home().parts[1] + '\\' + Path.home().parts[2]))
print(Path.cwd())
p = PurePath('SideProjects')

c = Path('\\Users\\Max\\PycharmProjects\\SideProjects')
for o in c.iterdir():
    print(o)
print(os.listdir('C:\\'))

print('\n')
# listdir and iterdir do the same thing
print(os.listdir('\\Users\\Max\\PycharmProjects\\SideProjects\\'))
print(PurePath('\\Users\\Max\\PycharmProjects\\SideProjects\\').parts)
print('\n')
print(os.listdir('D:\\'))
print(PurePath('\\Users\\Max\\PycharmProjects\\SideProjects\\').parent)
