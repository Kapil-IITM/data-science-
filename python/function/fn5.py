# Write a function to find the factorial of n (n is the parameter)



def cal_fact(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print(fact)

cal_fact(4)
cal_fact(5)
cal_fact(100)