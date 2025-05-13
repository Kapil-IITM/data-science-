# write a programme to find factorial of first n numbers. 
# 5! = 1*2*3*4*5

n = 5
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print("factorial =", fact)
