amount = input("How many terms of the Fibonacci sequence do you want?: ")


def fibonacci(num):
    num = str(num)
    print("You said you wanted " + num + " terms? Here you go: ")
    print()
    num = int(num)
    n1, n2 = 0, 1
    count = 0
    while count < num:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1


def ask():
    new_amount = input("Now how many do you want?: ")
    return new_amount


def tester(n):

    try:
        n = int(n)
    except ValueError:
        print("This not an integer please replace " + n)
        new_amount = input("so what do you want instead: ")
        tester(new_amount)
        return

    n = int(n)
    if n < 0:
        print("Sorry, cannot print a negative amount of numbers in the sequence")
        new_amount = input("so what do you want instead: ")
        tester(new_amount)
    elif n == 0:
        new_amount = input("you want me to print nothing... c'mon: ")
        tester(new_amount)
    elif n == 1:
        new_amount = input("come on that's boring: ")
        tester(new_amount)
    elif n == 2:
        new_amount = input("that's lame c'mon: ")
        tester(new_amount)
    else:
        fibonacci(n)


tester(amount)
