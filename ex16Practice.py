file = open("in.txt", "r")
print(file.read())
file.close()

file = open("in.txt", "w")
print("enter 3 lines : ")

line1 = input(" 1 : \n")
line2 = input(" 2 : \n")
line3 = input(" 3 : \n")
final = line1 + line2 + line3

file.write(final)
file.close()