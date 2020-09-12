
st = input().split()

s = int(st[0])

t = int(st[1])

ab = input().split()

a = int(ab[0])

b = int(ab[1])

mn = input().split()

m = int(mn[0])

n = int(mn[1])

apples = list(map(int, input().rstrip().split()))

oranges = list(map(int, input().rstrip().split()))

def countApplesAndOranges(s, t, a, b, apples, oranges):
    appcount = 0
    orrcount = 0
    for i in apples:
        # print('i is:')
        # print(i)
        if (i+a) in range(s,t+1):
            print('i+a is ',i+a)
            appcount = appcount +1


    for j in oranges:
        # print('j is: ',j)
        if (j + b) in range(s,t+1):
            #print('j + b is: ',j + b)
            orrcount = orrcount + 1

    print(appcount)
    print(orrcount)

countApplesAndOranges(s, t, a, b, apples, oranges)
