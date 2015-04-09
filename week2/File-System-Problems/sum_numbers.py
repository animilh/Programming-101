from sys import argv

file = open(argv[1],'r')
content = file.read().split(" ")
print (sum([int(num) for num in content]))
