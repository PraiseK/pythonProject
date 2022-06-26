# numbers = []
# for number in range(5):
#     total_number = int(input("Number: "))
#     numbers.append(total_number)
# print(numbers)
# print(f"The first number is {numbers[0]}")
# print(f"The last number is {numbers[-1]}")
# print(f"The smallest number is ", min(numbers))
# print(f"The largest number is ", max(numbers))
# print(f"The average of the numbers is {sum(numbers)/ 5}")

correct_usernames = usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']
username = input("Enter username: ")
if username in correct_usernames:
    print("Access granted")
else:
    print("Access denied")

