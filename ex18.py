# def print_two(*args):
#     arg1, arg2 =args
#     print("arg1: %r, arg2 :%r") % (arg1, arg2)

# ok. that *args is actually pointless , we can just do this
# fn likha hoy def diye, def er under e
def print_two_again(arg1, arg2):
    print ("arg1: %r, arg2: %r" % (arg1,arg2))
# fn er kaj likha holo ekhane

#this just takes one argument
def print_one(arg1):
    print ("arg1: %r" % arg1)

# this one takes no arguments
def print_none():
    print ("I got nothin'.")

# print_two("Zed","Shaw")
print_two_again("Zed","shaw") # fn call kora holo
print_one("first")
print_none()