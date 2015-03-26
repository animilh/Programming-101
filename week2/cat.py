from sys import argv

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    print(content)
    print('\n')
    file.close()

def main():
    for arg in argv[1:]:
        read_file(arg)

if __name__ == '__main__':
    main()
