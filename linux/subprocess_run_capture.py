import subprocess
import shlex
import platform


def run_command(command):
    command = shlex.split(command)
    print(f'command   | {command}')


    completed = subprocess.run(
        command,
        capture_output=True,        # save output to completed.stdout and/or completed.stderr
        text=True                   # save as text, not binary
    )

    # completed is a CompletedProcess object
    for k, v in vars(completed).items():
        print(f'completed | {k:15} | {v}')

run_command('date +%a')
run_command('date %a')
