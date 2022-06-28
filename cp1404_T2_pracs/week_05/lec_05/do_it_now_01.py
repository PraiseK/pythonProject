names = ['Cue Nguyen', 'Hellene Clinton', 'Sarah Edison']

ages = [50, 30, 20]



#

name_to_age = {'Cue Nguyen': 50, 'Hellene Clinton': 30, 'Sarah Edison': 20}



for key, value in name_to_age.items():

    print(key, value)



for key in name_to_age.keys():

    print(key)



for value in name_to_age.values():

    print(value)

name_to_age['Tony William'] = 34
print(name_to_age)

# CREATING A DICTIONARY, THEY ARE MUTABLE
my_dict = {}
my_dict['bill'] = 25
print(my_dict)

# CHECKING
for key in my_dict:
    print(my_dict)

# copying
name_to_age_1 = name_to_age.copy()

