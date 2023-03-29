import subprocess
import shlex

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)


def run_command(command):
    if is_windows():
        command = GitBash().get_command(command)
    tokenized = shlex.split(command)
    print(f'command   | {tokenized}')

    try:
        completed = subprocess.run(
            tokenized,
            capture_output=True,        # save output to completed.stdout and/or completed.stderr
            text=True,                  # save as text, not binary
            check=True                  # enable exceptions
        )
        # completed is a CompletedProcess object
        # completed.args      : tokenized command
        # completed.returncode: exit code
        # completed.stdout    : output stream
        # completed.sterr     : error stream
        for k, v in vars(completed).items():
            print(f'completed | {k:15} | {v}')
    except subprocess.CalledProcessError as cpe:
        print(f'ERROR | {cpe}')

run_command('date +%a')
run_command('date %a')
