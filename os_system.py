import os

from util.gitbash import get_gitbash_command

os_name, cmd = get_gitbash_command('date')
print(f'os_name   | {os_name}')
print(f'command   | {cmd}')

exit_code = os.system(cmd)

print(f'exit code | {exit_code}')
