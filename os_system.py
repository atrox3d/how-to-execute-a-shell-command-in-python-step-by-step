import os
import platform


def bash_command(cmd):
    os_name = platform.system().lower()
    if os_name == 'windows':
        os_prefix = r'"C:\Program Files\Git\bin\bash.exe" -c '
    else:
        os_prefix = ''

    command = f'{os_prefix}{cmd}'

    return os_name, command


os_name, cmd = bash_command('date')
print(f'os_name   | {os_name}')
print(f'command   | {cmd}')

exit_code = os.system(cmd)

print(f'exit code | {exit_code}')
