def to_digits(n):
    list = []
    str_num = str(n)
    for i in range(0, len(str_num)):
        list.append(int(str_num[i]))
    # for ch in str(n):
    #     list.append(ch)
    # a='123'
    # [x for x in a] -> ['1','2','3']
    # [int(x) for x in a] -> [1,2,3]
    # for ch in str(n):
    # return [int(x) for x in str_num]
    return list


def count_words(arr):
    return {word : arr.count(word) for word in arr}

def unique_words_count(arr):
    return len(set(arr))

def nan_expand(times):

    if times==0:
        return ""
    return "Not a "*times + "NaN"

def iterations_of_nan_expand(expanded):
    str_nan="Not a NaN"
    list=['NaN','Not','a']

    for word in expanded.split():
        if word not in list:
            return False

    if expanded == "":
        return 0

    if str_nan in expanded:
        return expanded.count('Not')

def sum_of_divisors(n):
    sum_div=0
    for i in range(1, n+1):
        if (n % i == 0):
            sum_div += i
    return sum_div


def is_prime(n):
    if n<=1:
        return False

    return sum_of_divisors(n) == n+1


def count_prime(n, p):
    count = 0
    while n % p == 0 and n != 1:
        n = n/p
        count += 1

    return count

def prime_factorization(n):
    result=[]
    divisors=[i for i in range(1, n+1) if n % i == 0 and is_prime(i)]

    return [(div, count_prime(n,div)) for div in divisors]

def take_same(list):
    result=[]
    result.append(list[0])
    start = 1
    end = len(list)
    while start < end:
        if list[start] == list[start-1]:
            result.append(list[start])
            start += 1
        else:
            break
    return result

def group(list):
    result = []
    while len(list) != 0:
        elem=take_same(list)
        result.append(elem)
        list = list[len(elem):]
    return result


def max_consecutive(items):
    return max([len(g) for g in group(items)])


from itertools import groupby

def groupby2(func, seq):
    groups = []
    uniquekeys = []
    dictt={}
    data = sorted(seq, key=func)
    for k, g in groupby(data, func):
        groups.append(list(g))      # Store group iterator as a list
        uniquekeys.append(k)
    for key in uniquekeys:
        dictt[key] = groups[key]
    print dictt


def prepare_meal(number):
    if number % 3 != 0 and number % 5 != 0:
        return ''
    return str('spam '*count_prime(number, 3)+'and eggs'*count_prime(number, 5)).rstrip()

def reduce_file_path(path):
    pass

def is_an_bn(word):
    if word == "":
        return True
    for letter in word:
        if letter not in ('a','b'):
            return False
    return str('a'*word.count('a')+'b'*word.count('a')) == word


def normalize_list(list):
    result = []
    for i in range(0,len(list)):
        if len(str(list[i])) == 1:
            result.append(list[i])
        else:
            result.extend(to_digits(list[i]))

    return result


def is_credit_card_valid(number):
    num_str = str(number)
    if len(num_str) % 2 == 0:
        return False
    num_list = [int(num_str[i]) for i in range(0, len(num_str))]
#    print (num_str)
    for i in range(0, len(num_list)):
        if i % 2 == 1:
            num_list[i] = num_list[i] * 2

    if sum(normalize_list(num_list)) % 10 == 0:
        return True

    return False


def reduce_file_path(path):
    result=[]
    parts=path.split('/')
    result=[part for part in parts if part not in ('.','')]
    for part in result[::-1]:
        if part == '..':
            if len(result)>1:
                result.pop()
            result.pop()
    return '/'+"/".join(result)


def goldbach(n):
    if n < 2 and n % 2 == 1:
        return ('','')
    result = []
    for i in range(2, n//2 + 1):
        if is_prime(i) and is_prime(n-i):
            result.append((i, n-i))

    return result


def magic_square(matrix):
    result = []
    suma = sum(matrix[0])
# check for rows
    result_row = [sum(row) for row in matrix]
    for num in result_row:
        if num != suma:
            return False

# check for colons
    for row in matrix:
        suma_col = 0
        for col in row:
            suma_col += matrix[col][row]
        if suma_col != suma:
            return False

# check for main diagonal
    main_diag = [matrix[row][row] for row in matrix]
    for num in main_diag:
        if num != suma:
            return False

# check for second diagonal
    sec_diag = [matrix[row][col] for row in matrix for col in row
    if row + col == len(matrix[0])-1]
    for num in sec_diag:
        if num != suma:
            return False

    return True

from datetime import *
def friday_years(start, end):
    if start < 1 and end > 9999:
	    return 0
    count = 0
    for year in range(start, end + 1):
        date_year = datetime(year, 1, 1)
        if (year % 4 == 0) and (date_year.weekday() in (3, 4)):
            count += 1
        elif year % 4 !=0 and date_year.weekday() == 4:
            count += 1
    return count


def main():
    print friday_years(1000, 2000)
    print friday_years(1753, 2000)
    print friday_years(1990, 2015)
    print (magic_square([[23, 28, 21], [22, 24, 26], [27, 20, 25]]))
    print (magic_square([[16, 23, 17], [78, 32, 21], [17, 16, 15]]))
#   print(is_credit_card_valid(79927398715))
#    groupby(data, keyfunc)
#    print (count_prime(1000,5))

if __name__ == '__main__':
    main()

#zshrc
