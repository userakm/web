def f(a, b, c, d):
    n = a
    if n > b:
        n = b
    if n > c:
        n = c
    if n > d:
        n = d
    print(n)
    
arr = list(map(int,input().split()))
f(arr[0], arr[1], arr[2], arr[3])