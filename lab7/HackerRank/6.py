if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())

max1, max2 = -100, -100

for i in range(0, len(arr)):
    if(arr[i] > max1): 
        max1 = arr[i]

for i in range(0, len(arr)):
    if(arr[i] > max2 and arr[i] < max1): 
        max2 = arr[i]

print (max2)
