NAME_FILE = "name.txt"
out_file = open(NAME_FILE, 'w')
user_name = input("Enter your name: ")
print(user_name, file=out_file)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read().strip()
in_file.close()
print("Your name is", name)

infile = open("numbers", 'r')
number1 = int(infile.readline())
number2 = int(infile.readline())
infile.close()
print(number1 + number2)


infile = open("numbers", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
infile.close()
print(total)


