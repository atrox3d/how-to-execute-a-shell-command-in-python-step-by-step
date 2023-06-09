import os

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)

if is_windows():
    bash = GitBash()
    command = bash.get_command('ping -n 5 localhost')
else:
    command = 'ping -c 5 localhost'

print(f'command   | {command}')
process = os.popen(command)

lines = process.readlines()
print(f'lines     | {lines}')

exit_code = process.close()
print(f'exit_code | {exit_code}')
