n = int(input())
a = list(map(int, input().split()))
total = 0
for x in a:
    total += x
left = 0
ans = -1
for i in range(n):
    if left == total - left - a[i]:
        ans = i
        break
    left += a[i]
print(ans)