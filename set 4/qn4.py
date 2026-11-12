s = input().strip()
p = input().strip()
n = len(s)
m = len(p)
if m > n:
    print("None")
else:
    need = [0] * 26
    have = [0] * 26
    for ch in p:
        need[ord(ch) - 97] += 1
    for i in range(m):
        have[ord(s[i]) - 97] += 1
    res = []
    if have == need:
        res.append(0)
    for i in range(m, n):
        have[ord(s[i]) - 97] += 1
        have[ord(s[i - m]) - 97] -= 1
        if have == need:
            res.append(i - m + 1)
    if len(res) == 0:
        print("None")
    else:
        print(*res)