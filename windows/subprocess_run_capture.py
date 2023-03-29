import subprocess
import shlex
import platform

from gitbash import GitBash

command = GitBash().get_command('ping -n 5 localhost')
tokenized = shlex.split(command)
print(f'command   | {tokenized}')

completed = subprocess.run(
    tokenized,
    capture_output=True,        # save output to completed.stdout and completed.stderr
    text=True                   # save as text, not binary
)

# completed is a CompletedProcess object
for k, v in vars(completed).items():
    print(f'completed | {k:15} | {v}')
