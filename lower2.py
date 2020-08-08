# n = int(input())
# mini = 100
#
# list = []
# for i in range(int(n)):
#     x = input()
#     list.append(x)
#     mini = min(x,mini)
#
# print(list)
#
# #
# # for i in list:
# #     if list[i] <= min:
# #         min = list[i]
#
# print(min)
#
#
#

python_students = []
new_list = []
for _ in range(int(input())):
    name = input()
    score = float(input())
    data = [name, score]
    python_students.append(data)


python_students.sort(key = lambda x: x[1]) # it takes all the input, and returns sorted element of index 1. x[1] er shapekkhe sort  # ekhane shob sorted element ase.
# ekhn dekhbe array er 2nd element minimum er shoman kina , karon ekta element repeat hote pare
minvalue = python_students[0][1] # 1st nested element er float value return kore jeta already sorted, min value ase ekhane
secondValue = 0
print(minvalue)
print(python_students)
for i in python_students:
    if(minvalue < i[1]):
        secondValue = i[1]
        break

for i in python_students:
    if(secondValue == i[1]):
        new_list.append(i[0])

new_list.sort()

for i in new_list:
    print(i)
