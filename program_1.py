def initials_generator(personsName):

    intia = personsName.split()
    first = intia[0]
    first_initial = first[0].upper()
    middle = intia[1]
    middle_initial = middle[0].upper()
    last = intia[2]
    last_initial = last[0].upper()

    return print(first_initial,'.',middle_initial,'.',last_initial,'.')

personsName = input('Enter your first, middle, and last name ')

initials = initials_generator(personsName)
print(initials)
