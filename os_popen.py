import os
import platform

from util.gitbash import GitBash

bash = GitBash()
command = bash.get_command('date')

output = os.popen(command)

print(f'{type(output) = }')                     # print class os.wrap_close
print(f'{output.__dict__ = }')                  # print contents of dict (_stream, _proc)

for k, v in output.__dict__.items():    # print each element (_io.TextIOWrapper, Popen)
    print(f'{k}: {v}')


# print contents of Popen
print(f'{output._proc.args = }')                # prints the command
print(f'{output._proc.returncode = }')          # returncode is still None

text = output.read()                    # executes command and gets output
print(f'{text = }')

exit_code = output.close()              # get real exit code
print(f'{exit_code = }')

print(f'{output._proc.returncode = }')          # 0-127
