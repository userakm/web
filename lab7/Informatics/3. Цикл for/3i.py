n = int(input())
i = 1
cnt = 0
for i in range(n):
    i = i + 1
    if(n%i == 0):
        cnt = cnt + 1
print(cnt)        