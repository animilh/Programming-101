def is_number_balanced(n):
    sum_l=0
    sum_r=0
    str_n=str(n)
    for i in range(0,len(str_n)//2):
        sum_l+=int(str_n[i])
        sum_r+=int(str_n[len(str_n)-i-1])
 
    return sum_l == sum_r

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


def matrix_bombing_plan(m):
    result={}
    rows=sum(1 for row in m)
    cols=sum(1 for num in m[0])
    
    for i in range(rows):
        for j in range(cols):
            result[(i,j)]=sum_matrix(m)-(sum(neighb_element(i,j,m))-sum_bomb(neighb_element(i,j,m),m[i][j]))
    return result  

def sum_matrix(matr):
    result=0

    for row in matr:
      result+=sum(row)

    return result 
#    return sum([sum(row) for row in matr])    


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print (matrix_bombing_plan(m))
    print (is_number_balanced(8098))

if __name__ == '__main__':
    main()                
