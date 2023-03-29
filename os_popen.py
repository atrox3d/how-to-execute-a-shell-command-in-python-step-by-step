import os
import platform

from util.gitbash import GitBash


def run_command(command):

    # get git bash to run command
    bash = GitBash()
    command = bash.get_command('date')
    print(f'command                 | {command}')

    # open command but does not execute it
    output = os.popen(command)

    # print output internals
    print(f'type(output)            | {type(output)}')              # print class os.wrap_close
    print(f'output.__dict__         | {output.__dict__}')           # print contents of dict (_stream, _proc)
    for k, v in output.__dict__.items():                            # print each element (_io.TextIOWrapper, Popen)
        print(f'output[{k:15}] |  {v}')
    # print contents of Popen
    print(f'output._proc.args       | {output._proc.args}')         # prints the command
    print(f'output._proc.returncode | {output._proc.returncode}')   # returncode is still None

    text = output.read()                                            # runs command and gets output
    print(f'text                    | {text }')

    exit_code = output.close()                                      # close command and get real exit code
    print(f'exit_code               | {exit_code}')

    print(f'output._proc.returncode | {output._proc.returncode}')   # 0-127


run_command('date')
