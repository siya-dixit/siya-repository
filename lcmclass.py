# this class needs no init like the factorial because of no defined properties :)

class leastcm:
    def __call__(self, a, b):
        if (a > b):
            maximum = a
        else:
            maximum = b
        while (True):
            if (maximum % a == 0 and maximum % b == 0):
                break
            maximum = maximum + 1
        return maximum

def lcm_run():
    #first test
    a = 3
    b = 5
    lcm = leastcm()
    result = lcm(a,b)
    print("="*60, "\nThe LCM of", a, "and", b, "is", result)

    #second test
    a = 50
    b = 100
    result = lcm(a,b)
    print("="*60, "\nThe LCM of", a, "and", b, "is", result)

    #third test
    a = 5
    b = 7
    result = lcm(a,b)
    print("="*60, "\nThe LCM of", a, "and", b, "is", result)
