#n = int(input())
#i = 1
#cnt = 0
#while i <= n:
#    num = int(input())
#    if(num == 0):
#        cnt += 1     
#    i += 1 
     
#print(cnt)

n = int(input())
cnt = 0
for i in range(n):
    num = int(input())
    if(num == 0):
        cnt += 1     
    i += 1
print(cnt)