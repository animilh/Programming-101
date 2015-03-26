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

    strobj=str(obj)
    n = len(strobj)
    for i in range(0, n//2):
    	if strobj[i] != strobj[n-1-i]:
    		return False
    return True


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


def to_number(digits):
    result=''
    for i in range(0,len(digits)):
        result = result + str(digits[i])

    int_result = int(result)

    # result=0
    # for digit in digits:

    #     result=result*10 + digit
    return int_result


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
    count_1=0
    bin_n=''
    while True:
        n+=1
        bin_n=bin(n)[2:]
        for i in range(0, len(bin_n)):
            if bin_n[i] == 1:
                count_1 += 1

        if palindrome(bin_n) and even(n):
            return n  

def odd(n):
    return n % 2 == 0

def even(n):
    return not odd(n)    


def main():
    print (next_hack(0))
    print (next_hack(6))
    print (next_hack(10))
    print (next_hack(8031))


if __name__ == '__main__':
    main()		rue

