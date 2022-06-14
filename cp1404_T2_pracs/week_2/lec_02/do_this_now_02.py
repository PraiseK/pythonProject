try:
    infile = open('cp111.csv', 'r')
# read one line at a time
    line_to_print = 2
    counter = 0
    for line in infile:
        counter += 1
        if counter == line_to_print:
            print(line.strip())
    infile.close()
except FileNotFoundError as err:
    print(f'Error:{err}')