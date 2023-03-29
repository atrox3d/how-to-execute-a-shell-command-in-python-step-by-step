import subprocess
import shlex
import platform

from gitbash import GitBash

command = GitBash().get_command('ping -n 5 localhost')
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
