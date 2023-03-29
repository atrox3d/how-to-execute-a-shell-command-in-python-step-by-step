import os
import platform

def run_command(cmd):

    print()
    print(f'os_name   | {platform.system()}')
    print(f'command   | {cmd}')

    """
    using os.system() we cannot save the output of
    the command but we can save its exit code
    """
    exit_code = os.system(cmd)

    print(f'exit code | {exit_code}')


# run some commands using bash or git bash, if installed
for command in 'date ls pwd error'.split():
    run_command(command)


run_command('ping -c 5 localhost')
