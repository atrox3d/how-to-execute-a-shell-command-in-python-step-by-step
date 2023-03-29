import os
import platform
from pathlib import Path


class GitBash:
    paths = [
        r'C:\Program Files (x86)\Git\bin\bash.exe',
        r'C:\Program Files\Git\bin\bash.exe'
    ]

    def __init__(self, *paths):
        self.paths.extend(paths)

        self.os = platform.system().lower()
        if self.os == 'windows':
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

        if self.os == 'windows':
            os_prefix = f'"{self.path}" -c '
            command = f'{os_prefix} "{cmd}"'
        else:
            command = cmd

        return command


if __name__ == '__main__':
    bash = GitBash(*'so many paths, man'.split())
    cmd = bash.get_command('ping -n 5 localhost')

    print()
    print(cmd)
    process = os.popen(cmd)
    output = process.read()
    exit_code = process.close()
    print(output)
    print(f'{exit_code = }')

    """
    os.system() needs extra double quoting!
    "c:\program files\git\bin\bash.exe" -c "command -args" 
    won't work!!!

    it needs to be all enclosed in double quotes:
    ""c:\program files\git\bin\bash.exe" -c "command -args""

    that's just horrible: http://ss64.com/nt/syntax-esc.html
    """
    cmd = f'"{cmd}"'
    print()
    print(cmd)
    exit_code = os.system(cmd)
    print(f'{exit_code = }')
