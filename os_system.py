import os
import platform

os_name = platform.system().lower()
if os_name == 'windows':
    cmd = r'"C:\Program Files\Git\bin\bash.exe" -c daet'
else:
    cmd = 'date'

print(f'os        | {os_name}')
print(f'command   | {cmd}')

exit_code = os.system(cmd)

print(f'exit code | {exit_code}')
