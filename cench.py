n = int(input())
#count = n.bit_count()
mx = -1e9
mn = 1e9
a = list(map(int, input().split()))
for i in range(n):
    mx = max(mx, a[i])
    mn = min(mn, a[i])
for i in range(n):
    if a[i] == mx:
        a[i] = mn
for i in range(n):
    print(a[i], end=' ')