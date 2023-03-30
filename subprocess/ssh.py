import sys, subprocess, shlex

args = iter(sys.argv[1:])
hostname = next(args, None) or input('Enter ssh host name or address: ')
remote_command = next(args, None) or input('Enter remote command: ')

command = shlex.split(f'ssh {hostname} {remote_command}')
print(f'{command = }')

ssh = subprocess.Popen(
                        command,
                        stdin=subprocess.PIPE,
                        stdout=subprocess.PIPE,
                        stderr=subprocess.PIPE,
                        text=True
)

"""
ssh.stdin.write(remote_command)
ssh.stdin.close()
stdout = ssh.stdout.read()
stderr = ssh.stderr.read()
"""
stdout, stderr = ssh.communicate()
print(f'{stdout = }')
print(f'{stderr = }')
print(f'{ssh    = }')
