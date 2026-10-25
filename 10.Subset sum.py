def Subsetsum(arr,l,t):
    #if target becomes 0
    if t == 0:
        return True

    #if length becomes 0 even after all calculations
    if l == 0:
        return False

    #using or for if the fist condition leads the target to negative value
    return Subsetsum(arr,l - 1, t - arr[l-1]) or Subsetsum(arr,l-1,t)

a = [2, 3, 7, 8]
t = int(input("Enter target sum: "))

print(Subsetsum(a, len(a), t))