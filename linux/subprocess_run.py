import subprocess
import shlex
import platform

command = shlex.split('ping -c 5 localhost')
print(f'command   | {command}')

"""
the output of the command is sent to the terminal
just like os.system()
"""
completed = subprocess.run(command)

# completed is a CompletedProcess object
print(f'completed | {completed}')

for k, v in vars(completed).items():
    print(f'completed | {k:15} | {v}')
