n = int(input())

scores = list(map(int, input().rstrip().split()))

def breakingRecords(scores):
    hcount = 0
    lcount = 0
    high = scores[0]
    low = scores[0]

    for i in scores:
        if i>high:
            high = i
            hcount +=1
        if i < low :
            low = i
            lcount +=1
    return hcount,lcount
result = breakingRecords(scores)
print(result)