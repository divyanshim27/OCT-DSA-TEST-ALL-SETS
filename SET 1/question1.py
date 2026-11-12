n = int(input())
prices = list(map(int, input().split()))
t = int(input())
seen = {}
for j in range(n):
    need = t - prices[j]
    if need in seen:
        print(seen[need], j)
        break
    seen[prices[j]] = j