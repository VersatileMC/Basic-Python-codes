def subsequences(s, ans=""):
    if s == "":
        print(ans)
        return

    #Reccursive printing all subsequences using current character "s[0]"
    subsequences(s[1:], ans + s[0])
    subsequences(s[1:], ans)

s = input("Enter string: ")
subsequences(s)