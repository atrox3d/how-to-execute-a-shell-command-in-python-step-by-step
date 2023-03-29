import os

command = 'ping -c 5 localhost'

print(f'command   | {command}')
process = os.popen(command)

lines = process.readlines()
print(f'lines     | {lines}')

exit_code = process.close()
print(f'exit_code | {exit_code}')
