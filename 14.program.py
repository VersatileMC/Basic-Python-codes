a = [1,3,5,7,9,11]
x = int(input("Enter element:"))

#initializing position at 0 firstly
position = 0

while position<len(a) and a[position]<x:
    position += 1
    
print("Element can be inserted at index:",position)