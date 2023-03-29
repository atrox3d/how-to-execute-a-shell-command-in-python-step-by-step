import platform
from pathlib import Path


def get_gitbash():
    paths = [
        r'C:\Program Files (x86)\Git\bin\bash.exe',
        r'C:\Program Files\Git\bin\bash.exe'
    ]

    found = False

    for path in paths:
        git_bash = Path(path)
        if git_bash.exists():
            found = True
            break

    if not found:
        newline = '\n'
        raise FileNotFoundError(f"cannot find git bash in:{newline}{newline.join([path for path in paths])}")

    return git_bash


def get_gitbash_command(cmd):
    """ tries to run command in git bash if under windows """

    os_name = platform.system().lower()
    if os_name == 'windows':
        git_bash = get_gitbash()
        # os_prefix = r'"C:\Program Files\Git\bin\bash.exe" -c '
        os_prefix = f'"{git_bash}" -c '
    else:
        os_prefix = ''

    command = f'{os_prefix}{cmd}'

    return os_name, command
