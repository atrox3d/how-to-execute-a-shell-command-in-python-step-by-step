import os


def run_command(command):
    exit_code = os.system(command)
    print(f'{command   = }')
    print(f'{exit_code = }')


ping = 'ping -c 5 localhost'

# run_command(windows_ping)
run_command(ping)

