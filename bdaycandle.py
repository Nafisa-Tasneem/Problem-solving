ar_count = int(input())

ar = list(map(int, input().rstrip().split()))

def birthdayCakeCandles(ar):
    maxi = 0
    cnt = 0
    for i in range (ar_count):
        if ar[i] > maxi:
            maxi = ar[i]

    for i in ar:
        if int(i) == maxi:
            cnt += 1
    return cnt


result = birthdayCakeCandles(ar)
print(result)