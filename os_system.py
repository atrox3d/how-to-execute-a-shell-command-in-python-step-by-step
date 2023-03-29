import os
import platform

from util.gitbash import GitBash


def run_bash_command(command):
    bash = GitBash()
    cmd = bash.get_command(command)

    print()
    print(f'os_name   | {bash.os}')
    print(f'command   | {cmd}')

    """
    using os.system() we cannot save the output of
    the command but we can save its exit code
    """
    exit_code = os.system(cmd)

    print(f'exit code | {exit_code}')


def run_windows_command(command):

    print()
    print(f'os_name   | {platform.system()}')
    print(f'command   | {command}')

    exit_code = os.system(command)

    print(f'exit code | {exit_code}')


# run some commands using bash or git bash, if installed
for command in 'date ls pwd error'.split():
    run_bash_command(command)

# run some windows commands
if platform.system() == 'Windows':
    for command in 'dir error'.split():
        run_windows_command(command)
