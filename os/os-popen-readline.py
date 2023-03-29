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

process = os.popen(command)

print(f'command   | {command}')
while line := process.readline():
    print(f'line      | {line!r}')

exit_code = process.close()
print(f'exit_code | {exit_code}')
