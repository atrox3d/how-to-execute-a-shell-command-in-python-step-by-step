import subprocess
import shlex
import platform

from gitbash import GitBash


def run_command(command):
    command = GitBash().get_command(command)
    tokenized = shlex.split(command)
    print(f'command   | {tokenized}')

    completed = subprocess.run(
        tokenized,
        capture_output=True,        # save output to completed.stdout and/or completed.stderr
        text=True                   # save as text, not binary
    )

    # completed is a CompletedProcess object
    for k, v in vars(completed).items():
        print(f'completed | {k:15} | {v}')

run_command('date +%a')
run_command('date %a')
