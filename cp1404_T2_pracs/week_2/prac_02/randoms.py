import random
print(random.randint(5, 20))  # line 1
print(random.randrange(3, 10, 2))  # line 2
print(random.uniform(2.5, 5.5))  # line 3


# smallest = 5    largest = 20
# smallest = 3    line 2 could not produce 4
# smallest = 2.5   largest = 5.5

print(random.randint(1, 100))