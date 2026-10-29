a = [1,3,5,7,9,11]
x = int(input("Enter element:"))

floor = None
ceil = None

#Iterating throughout the array
for i in a:
    #updating floor value everytime
    if i<=x:
        floor = i
    
    #updating ceil value only once 
    if i>=x and ceil == None:
        ceil = i
        
if floor == None and ceil == None:
    print("Element not found")
else:
    print("Floor:",floor)
    print("Ceil:",ceil)