# Search for a number X in this tuple using loops : (1,4,9,16,25,36,49,64,81,100)

tpl = (1,4,9,16,25,36,49,64,81,100)
x = 81
for num in tpl:
    if x == num:
        print("found",num)

        break
    else:
        print("not found")
    