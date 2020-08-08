n = int(input().strip())

arr = []

for _ in range(n):
    arr.append(list(map(int, input().rstrip().split())))

print(arr)
        
def diagonalDifference(arr):
    diag_pri = 0
    diag_sec = 0
    for i in range(0,n):
        for j in range(0,n):
            if i == j :
                # print(i,j)
                # print(arr[i][j])
                diag_pri = diag_pri + arr[i][j]

    for i in range(0, n):
        for j in range(0, n):
            if i + j == n-1:
                # print(i, j)
                # print(arr[i][j])
                diag_sec = diag_sec + arr[i][j]
    # print(diag_pri)
    # print(diag_sec)
    result = abs(diag_sec - diag_pri)
    return result


result = diagonalDifference(arr)
print(result)