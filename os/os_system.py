import os
import platform
import sys

sys.path.append(os.getcwd())    # works only from project root
try:
    from osutils.gitbash import GitBash
    from osutils.os_detect import (
        is_windows,
        is_linux,
        is_macos,
        os_name
    )
except ModuleNotFoundError:
    print('cannot import osutils.*')
    PYTHONPATH=os.environ.get('PYTHONPATH')
    print(f'{PYTHONPATH = }')
    print(f'{sys.path   = }')
    print("""
    SOLUTIONS:
    
    1) run with temporary PYTHONPATH set to project root:
        PYTHONPATH=path/to/ptoject/root python path/script.py
    
    2) export PYTHONPATH with project root set
        export PYTHONPATH=path/to/ptoject/root 
        python path/script.py
    
    3) insert '..', '...' at the beginning of sys.path
    """)
    exit(1)

def run_bash_command(command):
    if is_windows():
        bash = GitBash()
        cmd = bash.get_command(command)
        #
        # os.system() needs extra double quoting!
        #
        command = f'"{cmd}"'

    print()
    print(f'os_name   | {os_name}')
    print(f'command   | {command}')

    """
    using os.system() we cannot save the output of
    the command but we can save its exit code
    """
    exit_code = os.system(command)

    print(f'exit code | {exit_code}')


def run_windows_command(command):
    print()
    print(f'os_name   | {platform.system()}')
    print(f'command   | {command}')

    exit_code = os.system(command)

    print(f'exit code | {exit_code}')


# run some commands using bash or git bash, if installed
for command in 'date ls pwd error'.split():
    run_bash_command(command)

# run some windows commands
if is_windows():
    for command in 'dir error'.split():
        run_windows_command(command)

if is_windows():
    run_bash_command('ping -n 5 localhost')
else:
    run_bash_command('ping -c 5 localhost')
