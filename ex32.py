the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

for number in the_count: # numbr jodi count e thake tahole print korbe
    print("This is count %d" % number)

for fruit in fruits:
    print("A fruit of type : %s" %fruit)

for i in change:
    print("I got %r" % i)

elements = [] # empty list newa holo

for i in range(0, 6):
    print("Adding %d to the list." % i)
    # append is a function that lists understand
    elements.append(i)

for i in elements:
    print("Element was: %d" % i)

a = [1, 3, 6, 7, 6, 9, 0]
print(a)
print(a[2:5])
print(a[:4])
print(a[2:])
print(a[-4:-1])
a[2] = 8
print(a)
a.append(7)
print(a)
a.insert(1,2)
print(a)
a.remove(6)
print(a)
a.remove(7)
print(a)
a.pop()
print(a)
del a[4]
print(a)
# del a
# print(a) # ekhane kisu dekhabe na karon pura list del hoye gese
# a.clear()
# print(a)
b = a.copy()
print(b)
c = list(a)
d = a + b
print(d)
for s in b:
    c.append(s) # c te append kora holo

print(c)
e = [5, 6]
f = [0, 9]
e.extend(f)
print(e)
g = list((5, 6, 8))
print(g)