def fact(b):
    a = 1
    for i in range(1,b+1):
        a = a * i
    return a
b = 5
number = fact(b)
print("="*30)
print("The Factorial Of 5 Is: ", number)
print("="*30)
