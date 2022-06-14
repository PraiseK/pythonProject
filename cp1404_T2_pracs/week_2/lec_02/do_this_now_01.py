total_age = 0
num_of_people = 0
try:
    age = int(input("Enter age(-1 to quit): "))
    while age > -1:
        total_age += age
        num_of_people += 1
        age = int(input("Enter age(-1 to quit): "))
        average_age = total_age / num_of_people

    if num_of_people > 0:
        print("Average age of {} people is {:.2f}".format(num_of_people, total_age/num_of_people))
    else:
        print("No valid age entered")

except ValueError as err:
    print(f'Error:{err}')