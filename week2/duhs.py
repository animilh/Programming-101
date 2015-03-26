import os

def get_size(path):
    total_size = 0
    for roots, dirs, files in os.walk(path):
        for filename in files:
            file_path = os.path.join(roots, filename)
            if os.path.exists(file_path):
                total_size += os.path.getsize(file_path)
    return total_size * 10**(-9)   # size in GB


def main():
    print(get_size('/home/burnaski/code'))


if __name__ == '__main__':
        main()
