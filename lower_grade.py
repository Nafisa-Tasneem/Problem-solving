n = int(input())

student = []
minimum = 100
second_min = 100
for i in range(n):
    name = input()
    score = float(input())
    student.append([name,score])

    minimum = min(score,minimum)

for i in student:
    if i[1] != minimum:
        second_min= min(i, second_min)

print(second_min)

# for i in range(0,n):
#     minimum = min(minimum,student[i][1])
#     if student[i][1] == minimum:
#         student.remove()


print(student)
# x = sorted(student)[1]
# second_lower = x[1]
# print(second_lower)
# y =[]
# for j in range(n):
#     if student[j][1] == second_lower:
#          y.append(student[j][0])
#
# y.sort()
#
# for i in y:
#     print(i)

