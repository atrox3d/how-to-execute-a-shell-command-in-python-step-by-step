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

    completed = subprocess.run(
        tokenized,
        # capture_output=True,        # save output to completed.stdout and/or completed.stderr
        stdout=subprocess.PIPE,     # capture stdout
        # stderr=subprocess.PIPE,    # capture stderr
        stderr=subprocess.STDOUT,   # redirect stderr to stdout
        text=True                   # save as text, not binary
    )

    # completed is a CompletedProcess object
    # completed.args      : tokenized command
    # completed.returncode: exit code
    # completed.stdout    : output stream
    # completed.sterr     : error stream
    for k, v in vars(completed).items():
        print(f'completed | {k:15} | {v}')


run_command('date +%a')
run_command('date %a')
