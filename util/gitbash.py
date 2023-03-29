import platform
from pathlib import Path


class GitBash:
    paths = [
        r'C:\Program Files (x86)\Git\bin\bash.exe',
        r'C:\Program Files\Git\bin\bash.exe'
    ]

    def __init__(self, *paths):
        self.paths.extend(paths)

        for path in self.paths:
            self.git_bash = Path(path)
            if self.git_bash.exists():
                break
        else:
            newline = '\n'
            raise FileNotFoundError(
                f'cannot find git bash in:{newline}'
                f'{newline.join([path for path in self.paths])}'
            )

    def get_command(self, cmd):
        """ tries to run command in git bash if under windows """

        os_name = platform.system().lower()
        if os_name == 'windows':
            git_bash = self.git_bash
            # os_prefix = r'"C:\Program Files\Git\bin\bash.exe" -c '
            os_prefix = f'"{git_bash}" -c '
        else:
            os_prefix = ''

        command = f'{os_prefix}{cmd}'

        return os_name, command


if __name__ == '__main__':
    osname, cmd = GitBash(*'so many paths, man'.split()).get_command('ls')
    print(osname, cmd)
