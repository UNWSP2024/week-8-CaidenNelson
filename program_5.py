classes = {}
courses = int(input('How many courses would you like to add'))
for i in range(courses):
    key = input('What is the Course ID? ').upper()
    value = input('What is the name of the class? ')

    classes[key] = value
pick = input('what subject would you like to see? ').upper()
for key, value in classes.items():
        if key.startswith(pick):
            print(key,value)

