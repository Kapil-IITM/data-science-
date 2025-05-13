# def odd even

def odd_even():
    num = int(input("Enter a number:- "))
    if num % 2 == 0:
        print("even")
    else:
        print("odd")
    return num

user = odd_even()

print(user)
