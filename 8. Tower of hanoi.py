def hanoi(n, source, helper, destination):
    #base case for if disks reaches 0
    if n == 0:
        return 0

    #starting off
    hanoi(n-1,source,destination,helper)

    print("Move disk",n,"from",source,"to",destination)

    #back to destination
    hanoi(n-1,helper,source,destination)

n = int(input("Enter number of disks: "))
hanoi(n, "A", "B", "C")