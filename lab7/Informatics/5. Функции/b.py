def f(x, y):
    i = 1
    for i in range(y):
        i *= x
    print(i)
a = list(map(int,input().split()))
f(a[0],a[1])