import platform

os_name = platform.system().lower()


def is_windows():
    return os_name.startswith('windows')


def is_linux():
    return os_name.startswith('linux')


def is_macos():
    return os_name.startswith('darwin')
