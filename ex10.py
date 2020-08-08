tabby_cat = "\tI'm tabbed in." # assigning variable
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = '''
I'll do a list:
\t* Cat food 
\t* Fishies
\t* Catnip\n\t* Grass
'''
''' \t er jonno tab hocche, then baki string print hocche , with *
 last line e same line e \n \t dewar jonno new line+ tab holo
as by using 3 ", the same string prints, so as it is written in a line, so both 
\n and \t is used. '''

print (tabby_cat)
print (persian_cat)
print(backslash_cat)
print(fat_cat)


print(" an animal.")
print(" an \a animal.") # ascii bell
print(" an \b animal.") # ASCII backspace but to visual change is seen
print(" an \f animal.") #form feed
print(" an \n animal.") #new line
#print("an\N{name} animal.") doesn't work
print(" an \r animal.") #carriage return
print(" an \t animal.")
print(" an \v animal.") #doesn't work
print(" an \o15 animal.") #doesn't work
print(" an \x16 animal.") #doesn't work
print(" What is lotted \r can\'t be blotted.") # returns only string after \r

'''
while True:
    for i in ["/","_","|","\\","|"]:
        print ("%s\r" % i,) ''' #continuous loop

formatter_r = "%r %r"
formatter_s = "%s %s"
formatter_rs = "%r %s"

x = "Don\'t"
y = "\"Hey\"!"

print(formatter_r %(y,x)) # %r dile jei string disi exactly oitai ashe
print(formatter_s %(y,x)) # %s dile jerokom show koranor kotha ta kore
print(formatter_rs %(y,x))
