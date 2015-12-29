import sys
import os
from os.path import isdir, getsize


def _total_size(filepath, total_size):
        for item in os.listdir(filepath):
            itempath = os.path.join(filepath, item)
            if os.path.isfile(itempath):
                total_size += os.path.getsize(itempath)
            elif os.path.isdir(itempath):
                _total_size(itempath, total_size)
        return total_size


def main():
        total_size = os.path.getsize(sys.argv[1])
        print(_total_size(sys.argv[1], total_size))


if __name__ == '__main__':
    main()


