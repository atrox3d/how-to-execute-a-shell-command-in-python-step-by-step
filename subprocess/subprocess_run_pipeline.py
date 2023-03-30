import subprocess
import shlex
import os

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)


def run_command(command, stdin=None):
    if is_windows():
        command = GitBash().get_command(command)
    tokenized = shlex.split(command)
    print(f'command   | {tokenized}')

    completed = subprocess.run(
        tokenized,
        input=stdin,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,                  # save as text, not binary
    )

    return completed


run1 = run_command(f'cat {os.path.basename(__file__)}')
print(run1)
print()
run2 = run_command('grep -i import', stdin=run1.stdout)
print(run2)
