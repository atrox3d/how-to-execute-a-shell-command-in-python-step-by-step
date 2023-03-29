import os

from windows.gitbash import GitBash


def run_command(command):
    process = os.popen(command)
    output = process.read()
    exit_code = process.close()
    print(f'{command   = }')
    print(f'{output    = }')
    print(f'{exit_code = }')


bash_ping = GitBash().get_command('ping -n 5 localhost')
windows_ping = 'ping -n 5 localhost'

run_command(windows_ping)
run_command(bash_ping)

