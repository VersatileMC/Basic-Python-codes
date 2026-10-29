a = input("Enter brackets:")
stack = []

pairings = {
    ')':'(',
    ']':'[',
    '}':'{'
}

valid = True

for ch in a:
    if ch in "([{":
        stack.append(ch)
    elif ch in ")]}":
        if len(stack) == 0 or stack.pop() != pairings[ch]:
            valid = False
            break

if len(stack) != 0:
    valid = False
    
if valid:
    print("Valid")
else:
    print("Invalid")