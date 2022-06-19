MINIMUM_LENGTH = 7


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisks(password)


def print_asterisks(password):
    print('*' * len(password))


def get_password(MINIMUM_LENGTH):
    """gets valid password from user"""
    password = input(f"Enter password (should be above {MINIMUM_LENGTH} characters): ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password (should be above {MINIMUM_LENGTH} characters): ")
    return password


main()
