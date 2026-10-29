stack = []
minstack = []

def push(x):
    stack.append(x)
    
    if len(minstack) == 0:
        minstack.append(x)
    else:
        minstack.append(min(x,minstack[-1]))

def pop():
    if len(stack) > 0:
        minstack.pop()
        return stack.pop()
    
def getmin():
    if len(minstack) > 0:
        return minstack[-1]

l = list(map(int,input("Enter elements you would like to push with spaces:").split()))

for i in l:
    push(i)

print("Before pop:",getmin())

pop()

print("After pop:",getmin())


