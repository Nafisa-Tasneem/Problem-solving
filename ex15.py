''' #this portion is done by reza
file = open ("in.txt", "r")
name = file.read()
print (name)
file.close()

file = open ("in.txt", "w")
file.write("Rezaul")
file.close()


file = open ("in.txt", "r")
name = file.read()
print (name)
file.close()


txt = open("ex15sample.txt") #txt er moddhe file ta ana holo

print(" here is your file.")
print(txt.read()) #read kora holo

print("Type the filename again:")
file_again = input("> ") #i/p te file name newa holo

txt_again = open(file_again)

print(txt_again.read())
'''
file_name = open("in.txt")
print(file_name.read())

print("write the file name : ")
file2 = input(" > ") # keeping i/p in a variable
print(" again the file is : ")
file2_open = open(file2)
print(file2_open.read())

file_name.close()
#je file open korsi sheta close kora holo, shei variable ta close kora holo
file2_open.close()
