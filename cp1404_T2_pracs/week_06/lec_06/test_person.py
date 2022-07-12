from person import *
# define one
p = Person('Joanne', 20)
print('My name is', p.name)
print('My age is', p.age)
print(p)

# second object
p2 = Person('Praise', 20)
print('My name is', p2.name)
print('My age is', p2.age)
print(p2)

list_of_people = [Person('Sarah'), Person('Phuc', 20), Person('Tiri', 21)]
for person in list_of_people:
    print(person)
