from collections import Counter
n = int(input())
arr = list(map(int, input().rstrip().split()))
m = int(input())
brr = list(map(int, input().rstrip().split()))

def missingNumbers(arr, brr):
    new_list =[]
    for i in range(len(brr)):
        if brr[i]!= arr[i]:
            a= brr.pop(i)
            new_list.append(a)
    return (new_list)


    # c1 = Counter(brr)
    # c2 = Counter(arr)
    # diff = list((c1 - c2).elements())

    # print(diff)

result = missingNumbers(arr,brr)
print(result)