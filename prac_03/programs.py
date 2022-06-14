# 1.Tax
TAX_RATE_LOW = 0.05
TAX_RATE_HIGH = 0.1
TAX_THRESHOLD_LOW = 100
TAX_THRESHOLD_HIGH = 1000

print("Python Party Tax Program - Where Tax is a Party")
income = float(input("Income: $"))
if income<TAX_THRESHOLD_LOW:
    print("$0 tax")
    print("Take home pay is: $", income, sep="")
elif income<TAX_THRESHOLD_HIGH:
    total_tax = income * TAX_RATE_LOW
    print("Total tax is: $", total_tax, sep="")
    take_home_pay = income-total_tax
    print("Take home pay is: $", take_home_pay, sep="")
else:
    total_tax = income * TAX_RATE_HIGH
    print("Total tax is: $", total_tax, sep="")
    take_home_pay = income - total_tax
    print("Take home pay is: $", take_home_pay, sep="")

# 2. CAR INSURANCE
LOW_CUT = 18
HIGH_CUT = 25
age = int(input("Enter age: "))
if age < LOW_CUT:
    print("Hire refused")
elif age < HIGH_CUT:
    print("Insurance required")
else:
    print("Insurance not required")

# 3. SIMPLE PASSWORD CHECK
USER_PASSWORD = 12345
password = float(input("Enter password: "))
if password == USER_PASSWORD:
    print("Access granted")
else:
    print("Access denied")

# 4. DOG YEARS
FIRST_TWO_YEARS = 10.5
HUMAN_YEAR = 4
MINIMUM = 2
age = float(input("Age in human years: "))
if age > MINIMUM:
    later_age = age - MINIMUM
    early_years = MINIMUM * FIRST_TWO_YEARS
    total_age = later_age * HUMAN_YEAR
    dog_age = total_age + early_years
    str(print("Age in dog years ", dog_age, sep=""))
else:
    dog_age = age * 10.5
    str(print("Age in dog years ", dog_age, sep=""))

# 5. Rock of ages
age = int(input("Your age: "))
if age < 0:
    print("Invalid age!")
elif age < 5:
    print("Toddler")
elif age < 12:
    print("Infant")
elif age < 20:
    print("Teenager")
elif age < 50:
    print("Adult")
elif age <= 120:
    print("Senior")
else:
    print("Invalid age!")

# 6. SPEEDING FINES
speed_limit = int(input("Speed limit: "))
driver_speed = int(input("Your speed: "))
speed_over_limit = driver_speed - speed_limit
if speed_over_limit < 13:
    print("Total fine is $177")
elif speed_over_limit <= 20:
    print("Total fine is $266")
elif speed_over_limit <= 30:
    print("Total fine is $444")
elif speed_over_limit <= 40:
    print("Total fine is $622")
else:
    print("Total fine is $1245")




