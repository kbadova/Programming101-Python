# cat2.py
import sys


def main():
    for argument in sys.argv[1:]:
        with open(argument, 'r+') as data:
            print(data.read())
            data.write("\n")
            print(data.read())

if __name__ == '__main__':
    main()
