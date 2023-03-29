import subprocess
import shlex

from osutils.gitbash import GitBash


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
    # completed.args      : tokenized command
    # completed.returncode: exit code
    # completed.stdout    : output stream
    # completed.sterr     : error stream
    for k, v in vars(completed).items():
        print(f'completed | {k:15} | {v}')

run_command('date +%a')
run_command('date %a')
