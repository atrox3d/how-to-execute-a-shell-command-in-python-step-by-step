import os


def run_command(command):
    process = os.popen(command)
    output = process.read()
    exit_code = process.close()
    print(f'{command   = }')
    print(f'{output    = }')
    print(f'{exit_code = }')


ping = 'ping -c 5 localhost'

run_command(ping)

