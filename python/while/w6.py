# search for a number x in this tuple using loops: (1,4,9,16,25,49,64,81,100)

tpl = (1,4,9,16,25,36,49,64,81,100)
x = 49
idx = 0

while idx <= len(tpl)-1:
    if tpl[idx] == x:
        print("found at idx",idx)
    idx += 1
    print("finding...")

