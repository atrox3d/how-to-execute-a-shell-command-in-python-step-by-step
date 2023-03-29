import os

from windows.gitbash import GitBash


def run_command(command):
    #
    # os.system() needs extra double quoting!
    #
    command = f'"{command}"'
    exit_code = os.system(command)
    print(f'{command   = }')
    print(f'{exit_code = }')


bash_ping = GitBash().get_command('ping -n 5 localhost')
windows_ping = 'ping -n 5 localhost'

# run_command(windows_ping)
run_command(bash_ping)

