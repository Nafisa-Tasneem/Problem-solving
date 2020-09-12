def icecreamParlor(m, arr):
    for i in range(n):
        #print(arr[i])
        for j in range(1,n):
            #print(arr[i])
            if (arr[i]+ arr[j])== m and i !=j:
                return (i+1,j+1)
                break

t = int(input())

for t_itr in range(t):
    m = int(input())

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = icecreamParlor(m, arr)