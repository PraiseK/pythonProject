import operator

name_to_age = {"Bill": 21, "Jane": 4, "Jack": 56}
name = input('Enter your name: ')
age = int(input('Age your age: '))
name_to_age[name] = age
# for key, value in sorted(name_to_age.items()):
#     print(f"{key:10s}-{value:10d}")
sorted_name_to_age = dict(sorted(name_to_age.items(),

                                 key=operator.itemgetter(1), reverse=True))

for key, value in sorted_name_to_age.items():
    print(f'{key:10s}-{value:10d}')

# new dict
my_dict = {}
for key, age in name_to_age.items():
    if age < 25:
        my_dict[name] = age
