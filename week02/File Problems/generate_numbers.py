import sys
from random import randint


def main():
    with open(sys.argv[1], 'r+') as data:
            for j in range(0, int(sys.argv[2])):
                i = randint(1, 1000)
                print(i)
                data.write(str(i) + " ")

if __name__ == '__main__':
    main()
