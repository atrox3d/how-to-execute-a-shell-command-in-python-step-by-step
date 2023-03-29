import platform
from pathlib import Path


class GitBash:
    paths = [
        r'C:\Program Files (x86)\Git\bin\bash.exe',
        r'C:\Program Files\Git\bin\bash.exe'
    ]

    def __init__(self, *paths):
        self.paths.extend(paths)

        os_name = platform.system().lower()
        if os_name != 'windows':
            raise SystemError(f'{GitBash.__class__.__name__} is only available in Windows')

        for path in self.paths:
            self.path = Path(path)
            if self.path.exists():
                break
        else:
            newline = '\n'
            raise FileNotFoundError(
                f'cannot find git bash in:{newline}'
                f'{newline.join([path for path in self.paths])}'
            )

    def get_command(self, cmd):
        """ tries to run command in git bash if under windows """

        # os_prefix = r'"C:\Program Files\Git\bin\bash.exe" -c '
        os_prefix = f'"{self.path}" -c '
        command = f'{os_prefix}{cmd}'

        return command


if __name__ == '__main__':
    osname, cmd = GitBash(*'so many paths, man'.split()).get_command('ls')
    print(osname, cmd)
