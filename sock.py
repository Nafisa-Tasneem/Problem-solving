n = int(input())

ar = list(map(int, input().rstrip().split()))

def sockMerchant(n, ar):
    cnt = 0
    nmbr = []
    for i in range(1,101):
        c = ar.count(i)
        # print(c)
        if c != 0 and c / 2 >= 1 :
            nmbr.append(c)
    print(nmbr)
    temp = 0
    for i in nmbr:
        if int(i)% 2 == 0: # even number
            temp = int(i)/2 + temp
        else:
            temp = (int(i)-1)/2 + temp



    return int(temp)




result = sockMerchant(n, ar)
print(result)