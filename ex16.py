print("opening the file ...")
target = open("in.txt", "w") # write mode e open kora holo,
# target variable e rakha holo

print("truncating the file. good bye!")
target.truncate() # clearing the file

print("now i'm going to ask you for three lines.")

line1 = input("line 1: ") # taking input from user and putting it in line1 variable
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write(line1) # line1 ta write kora holo file e
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it.")
target.close() # closing the file 