def power(x,n):
    if n == 0:
        return 1

    #Repeatedly multiplies base n number of times for power
    return x * power(x,n-1)

x = int(input("Enter Base number: "))
n = int(input("Enter power number: "))

print("Resultant: ",power(x,n))