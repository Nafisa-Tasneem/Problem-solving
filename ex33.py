# i = 0
# numbers = [] # taking an empty list
#
# while i < 6:
#     print("At the top i is %d" % i)
#     numbers.append(i)
#
#     i = i + 1
#     print("Numbers now: ", numbers)
#     print("At the bottom i is %d" % i)
#
# print("the numbers: ") # loop shesh hole eta kaj korbe
#
# for num in numbers:
#     print(num, end=" ")



def add_to_list(ip): # trying with fn
    number = [] # array er name number
    for i in range (0,ip + 1,2):
        number.append(i)
    print(number)

add_to_list(7)

def add_while(x,increment):
    number = []
    j = 0
    while j <= x:
        number.append(j)
        j = j + increment
    print(number)

add_while(8,2)



