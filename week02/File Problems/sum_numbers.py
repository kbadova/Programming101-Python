import sys


def main():

    with open('numbers.txt', 'r') as data:
        print(sum(int(x) for x in data.read().split()))

if __name__ == '__main__':
    main()