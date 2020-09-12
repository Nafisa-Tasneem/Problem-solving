# binary search algo implementation

n= int(input("Enter the size of array: "))
arr =[]
for i in range(n):
    x = int(input())
    arr.append(x)

print(arr)
key = int(input("Enter the key to find: "))

low = 0
high = n-1
ans = -1

while(low <= high):
    mid = int((low + high) / 2)
    if key == arr[mid]:
        ans = mid
        break
    elif (key < arr[mid]):
        high = mid - 1
    else:
        low = mid + 1

print(ans)
