n, k = map(int, input().split())
a = list(map(int, input().split()))
last = {}
found = False
for i in range(n):
    x = a[i]
    if x in last and i - last[x] <= k:
        found = True
        break
    last[x] = i
if found:
    print("YES")
else:
    print("NO")