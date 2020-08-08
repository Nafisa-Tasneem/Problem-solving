# creating dictionaries
states = {
    "Oregon": 'OR', # assigning key and values
    "Florida": 'FL',
    'California': 'CA',
    'New York': "NY",
    'Michigan': 'MI'
}

cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}
# adding more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY States has: ", cities['NY'])
print("OR State has: ", cities['OR']) # key er value print korbe

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states['Florida'])

print('-' * 10)
print("Michigan has :", cities[states['Michigan']]) # nesting kora holo
print("Florida has:", cities[states['Florida']])

print('-' * 10)
for state, abbrev in states.items(): # key and value rakhar jonno variable newa holo
    print("%s is abbreviated %s " % (state, abbrev))

print('-' * 10)
for abbrev,city in cities.items():
    print("%s is abbreviated %s " % (abbrev, city))

print('-' * 10)
for state, abbrev in states.items(): # variable newa holo state , abbrev naame
    # dict er protita item niye kaj kora holo
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])) # city er vitor abbrev keyword jader key ,
    # ta print korbe

print('-' * 10)
state = states.get('Texas', None)

if not state:
    print("Sorry, no Texas.")

    city = cities.get('TX', 'Does Not Exist')
    print("The city for the state 'TX' is: %s" % city)

for i,j in cities.items(): # printing keys and values
    print("%s : %s" %(i,j))