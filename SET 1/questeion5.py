n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    idx = abs(a[i]) - 1
    if a[idx] > 0:
        a[idx] = -a[idx]
res = []
for i in range(n):
    if a[i] > 0:
        res.append(str(i + 1))
if len(res) == 0:
    print("None")
else:
    print(" ".join(res))