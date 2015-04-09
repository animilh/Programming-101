from random import randint
from sys import argv

def random_n(n):
    if n <= 0:
        return 0
    return [randint(1, 1000) for i in range(0, n)]


def main():
    file = open(argv[1],'r+')
    content = [str(num) for num in random_n(int(argv[2]))]
    file.write(" ".join(content))
    for line in file:
        print(line)


if __name__ == '__main__':
    main()
