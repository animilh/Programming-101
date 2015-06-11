def factorial(n):
	result=1
	if n == 0:
	    return result
	while n >= 1:
		result=result*n
		n-=1
	return result


def fibonacci(n):
    if n <= 0:
        return []

    if n == 1:
        return [1]

    if n == 2:
        return [1,1]

    F1=1
    F2=1
    result=[1,1]

    for i in range(3, n+1):
        Fn = F1 + F2
        F1 = F2
        F2 = Fn
        result.append(Fn)

    return result


def sum_of_digits(n):

    result = 0
    num = str(n)
    if n < 0:
        num=str(abs(n))

    for i in range(0,len(num)):
        result = result + int(num[i])

    return result


def fact_digits(n):
	result = 0
	num = str(n)
	for i in range(0,len(num)):
		result = result + factorial(int(num[i]))

	return result


def palindrome(obj):
    return str(obj)[::-1] == str(obj)


def to_digits(n):
    list = []
    str_num = str(n)
    for i in range(0, len(str_num)):
    	list.append(int(str_num[i]))

    return list


def to_number(digits):
    result=0
    for digit in digits:
        result=result*10 + digit

    return result


def fib_number(n):
    fib_list=fibonacci(n)
    return to_number(fib_list)


def count_vowels(str):
    count=0
    vowels_list=['a','e','i','o','u','y','A','E','I','O','U','Y']
    for i in range(0,len(str)):
        if str[i] in vowels_list:
            count += 1

    return count


def count_consonants(str):
    result_str = ''
    for i in range(0,len(str)):
        if str[i].isalpha():
            result_str+= str[i]
        else:
            continue
    return len(result_str) - count_vowels(result_str)


def char_histogram(string):
    result = {string[i] : string.count(string[i]) for i in range(0, len(string))}

    return result


def p_score(n):
    if palindrome(n):
        return 1

    rvrs_n = int(str(n)[::-1])
    return 1 + p_score(n + rvrs_n)


def is_increasing(seq):
    if len(seq) == 0:
        return False
    elif len(seq) == 1:
        return True
    else:
        for i in range(0, len(seq) - 1):
            if seq[i] >= seq[i + 1]:
                return False
        return True


def is_decreasing(seq):
    if len(seq) == 0:
        return False
    elif len(seq) == 1:
        return True
    else:
        for i in range(0, len(seq) - 1):
            if seq[i] <= seq[i + 1]:
                return False
        return True


def next_hack(n):
    while True:
        n+=1
        count_1=0
        bin_n=''
        bin_n=bin(n)[2:]
        for i in range(0, len(bin_n)):
            if bin_n[i] == 1:
                count_1 += 1

        if palindrome(bin_n) and odd(count_1):
            return n

def even(n):
    return n % 2 == 0


def odd(n):
    return not even(n)
