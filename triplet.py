n = int(input().strip())

a = list(map(int, input().rstrip().split()))

def pickingNumbers(a):
    count_arr = []

    for i in range(101):
        count_arr.append(a.count(i))

    maxm= 0
    for i in range(100):
        if count_arr[i]+count_arr[i+1]> maxm:
            maxm = count_arr[i]+count_arr[i+1]
    return maxm

result = pickingNumbers(a)
print(result)