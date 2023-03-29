import os

from util.gitbash import GitBash

os_name, cmd = GitBash().get_command('date')
print(f'os_name   | {os_name}')
print(f'command   | {cmd}')

exit_code = os.system(cmd)

print(f'exit code | {exit_code}')
