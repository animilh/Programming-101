from random import randint
from sys import argv

def random_n(n):
    if n <= 0:
        return 0
    return [randint(1, 1000) for i in range(0, n)]

def argv_check():
    if len(argv) < 3:
        return False
    return True

def main():
    if not argv_check():
        print("generate_numbers.py should be called with 2 arguments : python3.4 generate_numbers.py generate.txt 10")
    else:
        file = open(argv[1],'r+')
        content = [str(num) for num in random_n(int(argv[2]))]
        file.write(" ".join(content))
        for line in file:
            print(line)

if __name__ == '__main__':
    main()
