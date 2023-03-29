import subprocess
import shlex

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)

if is_windows():
    command = GitBash().get_command('ping -n 5 localhost')
else:
    command = GitBash().get_command('ping -c 5 localhost')
tokenized = shlex.split(command)
print(f'command   | {tokenized}')

"""
the output of the command is sent to the terminal
just like os.system()
"""
completed = subprocess.run(tokenized)

# completed is a CompletedProcess object
print(f'completed | {completed}')

for k, v in vars(completed).items():
    print(f'completed | {k:15} | {v}')
