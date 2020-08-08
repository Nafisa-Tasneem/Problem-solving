

class student:
    def __init__(self, initial_name, roll):
        self.name = initial_name
        self.roll = roll
    def get(self):
        print (self.name)
        print (self.roll)
    def changename(self, newname):
        self.name = newname

a = student('Nafisa', 1509032)
a.get()
b = student('Tahia', 10000)
b.get()

array = [a, b]
array[0].get()

