# write a programme to find factorial of first n numbers. 


# 5! = 1*2*3*4*5

n = 5

fact = 1

for i in range(1,n+1):
    fact *= i

print(f"factorial :- ",fact)