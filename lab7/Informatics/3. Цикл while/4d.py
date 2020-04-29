n = int(input())
s = 1
x = 0
while s <= n:
    s *= 2
    x += 1
    if s == n:
        print("YES")
        break
else:
    print("NO")