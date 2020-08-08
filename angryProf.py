first_multiple_input = input().rstrip().split()

n = int(first_multiple_input[0])

k = int(first_multiple_input[1])

s = list(map(int, input().rstrip().split()))

def nonDivisibleSubset(k, s):
    subset = set()

    for i in s:
        subset.add(i)

    for i in range (len(s)):
        # for j in range( i+1,len(s)):
        if i+1 < len(s):
            if (int(s[i])+int(s[i+1])) % k == 0 :

                print(s[i],s[i+1],int(s[i])+int(s[i+1]))
                subset.discard(s[i+1])
                subset.discard(s[i])
            # break

            # else:
                # print(s[i], s[j])
                # print((int(s[i])+int(s[j])) % k)
                # subset.add(s[i])


    # for i,j in s:
    #     if i!= j:
    #         if sum (int(s[i])+int(s [j]) )/k == 0:
    #             subset.add(s[j])
    print(subset,len(subset))
    return len(subset)

result = nonDivisibleSubset(k, s)
