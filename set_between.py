
first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

arr = list(map(int, input().rstrip().split()))

brr = list(map(int, input().rstrip().split()))


def getTotalX(a, b):
    maxm = 0
    for i in a:
        if i> maxm:
            maxm = i

    minm = 101
    for j in b:
        if j < minm:
            minm = j

    # print(maxm, minm)
    ans = 0
    for x in range(maxm, minm + 1):
        #if x can fulfil his conditions then
        x_is_a_candidate = True
        for i in a:
            if x % i != 0:
                x_is_a_candidate = False

        for i in b:
            if i % x != 0:
                x_is_a_candidate = False

        if x_is_a_candidate == True:
            ans += 1
        # print(x)

    return ans

y = getTotalX(arr, brr)
print(y)
    # if x % a[0] == 0 and x % a[1] == 0 and x % a[2] == 0 and b[0] % x == 0 ....
    # if x % a[0] != 0 or x % a[1] != 0 or x % a[2] != 0 or b[0] % x != 0..