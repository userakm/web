L = []
N = int(input())
for i in range(N):
    command = map(str,input().split())
    if command[0] == "sort":
        L.sort()
    elif command[0] == "print":
        print (L)
    elif command[0] == "reverse":
        L.reverse()
    elif command[0] == "pop":
        L.pop()
    elif command[0] == "insert":
        L.insert(int(command[1]),int(command[2]))
    elif command[0] == "append":
        L.append(int(command[1]))
    elif command[0] == "remove":
        L.remove(int(command[1]))