import os

from util.gitbash import GitBash

bash = GitBash()
cmd = bash.get_command('date')
print(f'os_name   | {bash.os}')
print(f'command   | {cmd}')

exit_code = os.system(cmd)

print(f'exit code | {exit_code}')
