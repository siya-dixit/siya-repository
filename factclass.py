class factorial:
    def __init__(self):
        self.factorial = []

    def __call__(self,n):
        if n == 1 or n == 0:
            self.print()
            return 1
        else:
            self.factorial.append(n)
            return n * self(n-1)

    def print(self):
        print("="*30, "\nSequence of Numbers: \n", *self.factorial)

def run_factorial():
    #first test
    n = 12
    facto = factorial()
    result = facto(n)
    print("="*30, "\nThe factorial of", n, "is", result)

    #second test
    n = 15
    facto = factorial()
    result = facto(n)
    print("="*30, "\nThe factorial of", n, "is", result)
