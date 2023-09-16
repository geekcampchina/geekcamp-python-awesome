import os
import sys

from happy_python import HappyLog
from happy_python.happy_log import HappyLogLevel

hlog = HappyLog.get_instance()
hlog.set_level(HappyLogLevel.TRACE.value)


def get_list(input_path):
    # ~/Downloads/ISO
    os.chdir(input_path)

    dirs = os.listdir()

    for path in dirs:
        if os.path.isdir(path):
            get_list(path)

        hlog.var('path', os.path.abspath(path))

    # ~/Downloads/ISO/..
    # ~/Downloads/
    os.chdir('..')


def main():
    spec_dir = sys.argv[1]

    # ~/Downloads
    get_list(spec_dir)


if __name__ == '__main__':
    main()
