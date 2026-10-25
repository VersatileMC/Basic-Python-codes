def fibonacci(n):
    #Base case
    if n <= 1:
        return n

    #actual formula
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input("Enter a number: "))
print("Fibonacci number for",n,"is:", fibonacci(n))