a = [1,2,2,2,3,4,5,5,6,7,7]
x = int(input("Enter element to search: "))

# Initializing first and last occurance to some value firstly
first = -1
last = -1

# Loop for interating throughout the array
for i in range((len(a))):
    #If element is found
    if a[i] == x:
        #only update first value once
        if first == -1:
            first = i
        
        #updating last value index everytime element matches
        last = i
        
#Checking to see if element was actually found in the first place
if first == -1 and last == -1:
    print("Element not found")
else:
    #printing first and last occurance 
    print("First occurance:",first)
    print("Last occurance:",last)
