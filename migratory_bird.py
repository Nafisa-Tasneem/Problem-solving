

arr_count = int(input().strip())

arr = list(map(int, input().rstrip().split()))

def migratoryBirds(arr):

    # for i in arr:
    cnt = []
    for number in range(1,6):
        cnt.append(arr.count(number)) # ekta number kotobar ase check korlam

    maxm = 0
    for i in cnt:
        if int(i) > maxm:
            maxm = i

    maxm_index = []
    for number in range(1,6):
        if arr.count(number) == maxm:
            maxm_index.append(number)

    mini = 6
    for i in maxm_index:
        if int(i) < mini:
            mini = i

    # print(cnt,maxm,maxm_index, mini)
    return mini

result = migratoryBirds(arr)
print(result)