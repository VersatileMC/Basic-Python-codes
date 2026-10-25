def printnum(n):
    if n == 0:
        return 0

    #Reccursion
    printnum(n-1)
    print(n)

n = int(input("Enter a number: "))
printnum(n)