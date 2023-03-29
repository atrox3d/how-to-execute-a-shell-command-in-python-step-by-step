import os

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)


def run_command(command):
    process = os.popen(command)
    output = process.read()
    exit_code = process.close()
    print(f'{command   = }')
    print(f'{output    = }')
    print(f'{exit_code = }')


if is_windows():
    bash_ping = GitBash().get_command('ping -n 5 localhost')
    windows_ping = 'ping -n 5 localhost'

    run_command(windows_ping)
    run_command(bash_ping)
else:
    run_command('ping -c 5 localhost')

