import os
import platform

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)


def run_bash_command(command):
    if is_windows():
        bash = GitBash()
        cmd = bash.get_command(command)
        #
        # os.system() needs extra double quoting!
        #
        command = f'"{cmd}"'

    print()
    print(f'os_name   | {os_name}')
    print(f'command   | {command}')

    """
    using os.system() we cannot save the output of
    the command but we can save its exit code
    """
    exit_code = os.system(command)

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
if is_windows():
    for command in 'dir error'.split():
        run_windows_command(command)

if is_windows():
    run_bash_command('ping -n 5 localhost')
else:
    run_bash_command('ping -c 5 localhost')
