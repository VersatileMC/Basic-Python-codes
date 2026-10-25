def permutations(s, ans=""):
    if s == "":
        print(ans)
        return

    for i in range(len(s)):
        permutations(s[:i] + s[i+1:], ans + s[i])

s = input("Enter string: ")
permutations(s)