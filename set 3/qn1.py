s = input()
i = 0
j = len(s) - 1
ok = True
while i < j:
    while i < j and not s[i].isalnum():
        i += 1
    while i < j and not s[j].isalnum():
        j -= 1
    if s[i].lower() != s[j].lower():
        ok = False
        break
    i += 1
    j -= 1
if ok:
    print("YES")
else:
    print("NO")