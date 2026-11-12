n = int(input())
ids = list(map(int, input().split()))
seen = set()
ans = -1
for x in ids:
    if x in seen:
        ans = x
        break
    seen.add(x)
print(ans)