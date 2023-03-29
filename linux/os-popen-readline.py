import os

command = 'ping -c 5 localhost'
process = os.popen(command)

print(f'command   | {command}')
while line := process.readline():
    print(f'line      | {line!r}')

exit_code = process.close()
print(f'exit_code | {exit_code}')
