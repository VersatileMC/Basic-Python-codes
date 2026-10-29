a = list(map(int,input("Enter elements for first array with spaces:").split()))
b = list(map(int,input("Enter elements for second array with spaces:").split()))

#Initializing initial values for i and j and making a new array c for storing sorted array
c = []
i = 0
j = 0

#appending elements to c based on comparision
while i<len(a) and j<len(b):
    if a[i] < b[j]:
        c.append(a[i])
        i += 1
    else:
        c.append(b[j])
        j += 1

#appending the rest of the arrays
while i<len(a):
    c.append(a[i])
    i += 1
    
#appending the rest of the arrays
while j<len(b):
    c.append(b[j])
    j += 1
    
#printing sorted array
print("Merged array:",c)