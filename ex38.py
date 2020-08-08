ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there's not 10 things in that list, let's fix that.")

stuff = ten_things.split(' ') # string k split kore list banabe. ekhane separator
# define kora holo. separator ' '
more_stuff = ["Day", "Night", "song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10: # jotokhon na stuff er len 10 hoy
    next_one = more_stuff.pop() # more_stuff er last element pop kora holo, sheta next_one e rakha holo
    print("Adding: ",next_one)
    stuff.append(next_one) # stuff e append kora holo last element of next_one
    print("There's %d items now." % len(stuff))

print("There we go: ", stuff) # loop shesh hole whole stuff print hobe.

print("Let's do something with stuff.")

print(stuff[1])
print(stuff[-1])
print(stuff.pop()) # je element pop kora holo ta print kora hobe
print(' '.join(stuff)) # list er element niye string return kore. majhe separator holo ' '
print('#'.join(stuff[3:5])) # list er 3,4 element niye join kore string return korbe
