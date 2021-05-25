# program to display the Fibonacci sequence up to n term
def fibonacci(n):
    a, b = 0, 1
    i = 0
    print("Fibonacci sequence up to {0}:".format(nterms))
    while i < nterms:
        print(a)
        # update values
        a, b = b, a+b
        i += 1

nterms = int(input("How many terms? "))
fibonacci(nterms)

# Python program to display the Fibonacci sequence by using recursion
def recur_fibonacci(n):
    return n if n <= 1 else recur_fibonacci(n-1) + recur_fibonacci(n-2)

print("With recursion:")
for i in range(nterms):
    print(recur_fibonacci(i))