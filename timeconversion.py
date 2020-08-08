s = input()

def timeConversion(s):

    arr = s.split(sep= ':')
    arr2 = list(arr[2])
    arr2.pop()
    ap = arr2.pop() # returns A or P
    arr2_new = ''.join(arr2)
    arr[2] = arr2_new
    # print(arr2_new)
    if ap == 'P' and arr[0] != '12':
        arr[0] = str(int(arr[0]) + 12)
    if arr[0] =='12' and ap =='A':
        arr[0] = '00'

    militime = ':'.join(arr)
    return militime

result = timeConversion(s)
print(result)
