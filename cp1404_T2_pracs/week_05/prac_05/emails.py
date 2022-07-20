email_to_name = {}
email = input("Email: ")
while email != "":
    name = email.split('@')[0]
    confirm = input(f"Is your name {name} (Y/n): ")
    if confirm != 'Y' and confirm != '':
        name = input("Name: ")
    email_to_name[email] = name
    email = input("Email: ")



