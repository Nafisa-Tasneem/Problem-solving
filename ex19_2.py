# def cheese_and_crackers(cheese_count, boxes_of_crackers):
#     print("u have %d boxes cheeses." % cheese_count )
#     print(" u have %d boxes of crackers." % boxes_of_crackers)
#     print(" enough")
#     print("Get a blanket.\n")

def print_calc(x,y,z):
    print("x : %r, y : %r , z : %r " %(x, y, z))
    summ = x + y + z
    print(summ)

# cheese_and_crackers(10, 20) # nije theke ip dite pari
#
# cheese = 10
# crackers = 50
#
# cheese_and_crackers(cheese, crackers) # alada variable pass korte pari
#
# cheese_and_crackers(10 + 2, 5 + 6)
#
# cheese_and_crackers(cheese +100 , crackers + 1000)

print_calc(10,20,30)

a = int(input(" Enter x:" ))
b = int(input(" Enter y:" ))
c = int(input(" Enter z:" ))

print_calc(a,b,c)