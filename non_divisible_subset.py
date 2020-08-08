first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))

def nonDivisibleSubset(k, s):
    subset = set()
    for a in s:
        subset.add(a)

    arr = []
    for a in subset:
        arr.append(a % k)
    print(arr)

    cnt = []
    for i in range(k):
        arr.count(i)
        cnt.append(arr.count(i)) # protita modulus koybar ase tar count

    x = sorted(cnt) # protita modulus k sorted akare ache

    print(cnt)
    count = 0
    # for i in range(k-1) :
    #     if s

def solveSubset(s, k):
    r = [0] * k

    for value in s:
        r[value % k] += 1

    print(r) # r e count er kaj korse
    result = 0
    for a in range(1, (k + 1) // 2):
        result += max(r[a], r[k - a])
    if k % 2 == 0 and r[k // 2]:
        result += 1
    if r[0]:
        result += 1
    return result

result = solveSubset(s, k)
