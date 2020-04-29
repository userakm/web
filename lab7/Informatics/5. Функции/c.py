def f(a, b):
    if a == b:
        return 0
    else:
        return 1
arr = list(map(int,input().split()))
print(f(arr[0], arr[1]))