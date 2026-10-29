a = list(map(int,input("Enter elements with spaces:").split()))

#Iterating throughout the array
for i in range(len(a)):
    #iterating from the alternative element to i for checking
    for j in range(i+1,len(a)):
        #Finding only one greater value hence the use of break
        if a[j] > a[i]:
            greater = a[j]
            break
    
    #Printing next greater value for every element in array
    print(a[i], "next greater value ->", greater)