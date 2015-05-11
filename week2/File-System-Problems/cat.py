from sys import argv

def read_file(filename):
    file = open(filename, "r")
    content = file.read()
    print(content)
    print('\n')
    file.close()

def argv_check():
    if len(argv) < 2:
        return False
    return True

def main():
    if not argv_check():
        print("cat.py should be called with at least 1 argument : python3.4 cat.py filename1 filename2")
    else:
        for arg in argv[1:]:
            read_file(arg)

if __name__ == '__main__':
    main()
