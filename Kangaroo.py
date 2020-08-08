import math

# a very important code for me

n = input()
x = ''.join(n.split()) # removing space from the string, first splitting, then joining
length =len(x)
root = math.sqrt(length)
row = math.floor(root)
colm = math.ceil(root)

if row * colm < length :
    row += 1

s = ''
for i in range (0,row+1): # joto row toto gula vaag kortesi, proti row te clm shonkhak element
    s =  s + x [colm* i : colm *(i+1) ] +' ' # adding space to string at proper place

matrix_2d = s.split()
len2 = len(matrix_2d)

while(len(matrix_2d[len2-1]) < colm): # making last element of this matrix length = colm

    matrix_2d[len2-1] = matrix_2d[len2-1] + ' '

final = []
for i in range(colm) :
    word =''
    for j in matrix_2d:

        word = word + j[i]
    final.append(word)
new_final = []

for i in final:
    x= i.rstrip() # removing extra space from each element
    new_final.append(x)

result = ' '.join(new_final)
print(result)

