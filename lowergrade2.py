# this is the final code which was submitted
n = int(input())
student = []
lower2 = 100
for i in range(n):
    name = input()
    score = float(input())
    student.append([name, score])

student.sort(key= lambda x:x[1])
minimum = student[0][1]

#print(student)
for i in student: # accessing each element
    if minimum < i[1]:
        lower2 = i[1]
        break
#print(lower2)

y = []

for j in range(n):
    if student[j][1] == lower2:
         y.append(student[j][0])

y.sort()
#print(y)

for i in y:
    print(i)




