a = [1,2,2,2,3,4,5,5,6,7,7]
x = int(input("Element to search for:"))

count = 0

for i in range(len(a)):
    if a[i] == x:
        count += 1
        
if count == 0:
    print("Element not found")
else:
    print("Count:",count)