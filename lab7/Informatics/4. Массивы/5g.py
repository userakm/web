n = int(input())
cnt = 0
arr = list(map(int, input().split()))
for i in range(n):
    print(arr[n-i-1], end = ' ')