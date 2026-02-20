n = int(input())
count = n.bit_count()
if count == 1:
    print("YES")
else:
    print("NO")