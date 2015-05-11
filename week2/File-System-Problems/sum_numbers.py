from sys import argv

if len(argv) < 2:
    print("generate_numbers.py should be called with 1 argument : python3.4 sum_numbers.py numbers.txt")

else:
    file = open(argv[1],'r')
    content = file.read().split(" ")
    print (sum([int(num) for num in content]))
