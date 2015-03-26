def sum_of_divisors(n):
    return sum([x for x in range(1, n + 1) if n % x == 0])


def count_of_divisors(n):
    return sum([1 for x in range(1, n + 1) if n % x == 0])


def is_prime(n):
    return n + 1 == sum_of_divisors(n)


def prime_number_of_divisors(n):
    is_prime(count_of_divisors(n))


def to_digits(n):
    return [int(x) for x in str(n)]


def contains_digit(number, digit):
    return digit in to_digits(number)


def contains_digits(number, digits):
    for digit in digits:
        if not contains_digit(number, digit):
            return False

    return True


def count_digits(n):
    return sum([1 for x in to_digits(n)])


def to_number(digits):
    result = 0

    for digit in digits:
        digits_count = count_digits(digit)
        result = result * (10 ** digits_count) + digit

    return result


def is_number_balanced(n):
    numbs = to_digits(n)
    half = len(numbs) // 2

    left_numbs = numbs[0:half]
    if len(numbs) % 2 == 0:
        right_numbs = numbs[half:]
    else:
        right_numbs = numbs[half + 1:]

    return sum(left_numbs) == sum(right_numbs)


def count_substrings(haystack, needle):
    return haystack.count(needle)


def zero_insert(n):
    result = []
    digits = to_digits(n)

    start = 0
    end = len(digits)

    while start < end - 1:
        x = digits[start]
        y = digits[start + 1]

        result.append(x)

        if (x + y) % 10 == 0 or x == y:
            result.append(0)

        start += 1

    result.append(digits[start])

    return to_number(result)


def sum_matrix(matr):
    result = 0

    for row in matr:
        result += sum(row)

    return result


def sum_matrix2(matr):
    # Using list comprehensions
    return sum([sum(row) for row in matr])

# function neighb_element(i,j,m) returns a list of neibourghs of an element (i,j) from matrix m

def neighb_element(i,j,m):
    rows=sum(1 for row in m)
    cols=sum(1 for num in m[0])
    result=[]
    for row in range(i-1, i+2):
        for col in range(j-1, j+2):
            if 0<=row<rows and 0<=col<cols:
                result.append(m[row][col])

    result.remove(m[i][j])
    return result

#  sum_bomb(list,bomb_num) returns the sum of bombed list of numbers, the bomb is bomb_num :)

def sum_bomb(list,bomb_num):
    result=[]
    for i in range(0,len(list)):
        if list[i]<=bomb_num:
            result.append(0)
        else:
            result.append(list[i]-bomb_num)

    return sum(result)


def matrix_bombing_plan (m):
    result={}
    rows=sum(1 for row in m)
    cols=sum(1 for num in m[0])

    for i in range(rows):
        for j in range(cols):
            result[(i,j)]=sum_matrix(m)-(sum(neighb_element(i,j,m))-sum_bomb(neighb_element(i,j,m),m[i][j]))
    return result

# from copy import deepcopy
# a[[1,2,3]]
# b = deepcopy(a)
