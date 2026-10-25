def digitsum(n):
    if n == 0:
        return 0

    #Taking last digit and adding that to reccursive calls with remaining digits
    return (n%10) + digitsum(n//10)

n = int(input("Enter a number: "))
print("Sum of digits of",n,"is:",digitsum(n))