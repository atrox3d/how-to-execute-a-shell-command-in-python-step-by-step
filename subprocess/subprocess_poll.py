import subprocess, shlex, time

from osutils.gitbash import GitBash
from osutils.os_detect import *


command = 'ping -n 5 localhost' if is_windows() else 'ping -c 5 localhost'
print(f'{command = }')

ping = subprocess.Popen(
    shlex.split(command),
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

while (exit_code := ping.poll()) is None:
    print(f'{exit_code = }')
    time.sleep(1)

print(f'{exit_code = }')
stdout, stderr = ping.communicate()
print(f'{stdout = }')
print(f'{stderr = }')
