import subprocess
import shlex
import platform


command = shlex.split('ping -c 5 localhost')
print(f'command   | {command}')


completed = subprocess.run(
    command,
    capture_output=True,        # save output to completed.stdout and completed.stderr
    text=True                   # save as text, not binary
)

# completed is a CompletedProcess object
for k, v in vars(completed).items():
    print(f'completed | {k:15} | {v}')
