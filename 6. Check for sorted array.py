def sorted(arr):
    #For the last case if all positions is checked and it evaluates to true
    if len(arr) <= 1:
        return True

    #For immediately flagging it as False
    if arr[0] > arr[1]:
        return False

    #Working throughout the array
    return sorted(arr[1:])

#user input array
array = list(map(int,input("Enter numbers seperated by spaces:").split()))

if sorted(array):
    print(array,"is sorted")
else:
    print(array,"is not sorted")