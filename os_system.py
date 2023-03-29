import os
import platform

from util.gitbash import GitBash

cmd = GitBash().get_command('date')
print(f'os_name   | {platform.system()}')
print(f'command   | {cmd}')

exit_code = os.system(cmd)

print(f'exit code | {exit_code}')
