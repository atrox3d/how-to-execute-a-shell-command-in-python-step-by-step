import os

from util.gitbash import GitBash


def run_command(command):
    bash = GitBash()
    cmd = bash.get_command(command)

    print()
    print(f'os_name   | {bash.os}')
    print(f'command   | {cmd}')

    exit_code = os.system(cmd)

    print(f'exit code | {exit_code}')


for command in 'date ls pwd that\'s an error'.split():
    run_command(command)
