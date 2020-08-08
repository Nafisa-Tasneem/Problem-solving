def hackerrankInString(s):

    str = 'hackerrank'
    cnt = 0
    for j in str:
        for i in s:
            print(j,i)
            if i == j:
                cnt += 1
                break
            

    if cnt == 10:
        var = "YES"
    else:
        var = 'NO'
    return var


    # if 'hackerrank' in s:
    #     print('YES')
    # else:
    #     print('NO')

q = int(input())

for q_itr in range(q):
    s = input()

    result = hackerrankInString(s)
    print(result)
