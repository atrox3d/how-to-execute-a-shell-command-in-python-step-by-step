import subprocess
import shlex

from osutils.gitbash import GitBash
from osutils.os_detect import (
    is_windows,
    is_linux,
    is_macos,
    os_name
)


def run_command(command, file_prefix=None):
    if is_windows():
        command = GitBash().get_command(command)
    tokenized = shlex.split(command)
    print(f'command   | {tokenized}')

    if file_prefix:
        stdout_filename = f'{file_prefix}_out.txt'
        stderr_filename = f'{file_prefix}_err.txt'
    else:
        stdout_filename = 'stdout.txt'
        stderr_filename = 'stderr.txt'
    with (
        open(stdout_filename, 'w') as stdout_file,
        open(stderr_filename, 'w') as stderr_file
    ):
        completed = subprocess.run(
            tokenized,
            stdout=stdout_file,
            stderr=stderr_file,
            text=True                   # save as text, not binary
        )

    # completed is a CompletedProcess object
    # completed.args      : tokenized command
    # completed.returncode: exit code
    # completed.stdout    : output stream
    # completed.sterr     : error stream
    for k, v in vars(completed).items():
        print(f'completed | {k:15} | {v}')


run_command('date +%a', file_prefix='date_ok')
run_command('date %a', file_prefix='date_err')
