import random


states = {'Minnesota':'St Paul', 'Washington':'Olympia','Alabama':'Montgomery','Alaska':'Juneau','Arizona':'Phoenix','Arkansas':'Little Rock',
          'California':'Sacramento', 'Colorado':'Denver', 'Connecticut':'Hartford','Delaware':'Dover','Florida':'Tallahassee','Georgia':'Atlanta','Hawaii':'Honolulu',
          'Idaho':'Boise','Illinois':'Springfield','Indiana':'Indianapolis','Iowa':'Des Moines','Kansas':'Topeka','Kentucky':'Frankfort','Louisiana':'Baton Rouge',
          'Maine':'Augusta','Maryland':'Annapolis','Massachusetts':'Boston','Michigan':'Lansing','Mississippi':'Jackson','Missouri':'Jefferson City','Montana':'Helena',
          'Nebraska':'Lincoln','Nevada':'Carson City','New Hampshire':'Concord','New Jersey':'Trenton','New Mexico':'Santa Fe','New York':'Albany','North Carolina':'Raleigh',
          'North Dakota':'Bismark','Ohio':'Columbus','Oklahoma':'Oklahoma City','Oregon':'Salem','Pennsylvania':'Harrisburg','Rhode Island':'Providence','South Carolina':'Columbia',
          'South Dakota':'Pierre','Tennessee':'Nashville','Texas':'Austin','Utah':'Salt Lake City','Vermont':'Montpelier','Virginia':'Richmond','West Virgina':'Charleston',
          'Wisconsin':'Madison','Wyoming':'Cheyenne'  }

total_correct = 0
total_wrong = 0
count = 0
while count < 50:
    count+=1
    state = random.choice(list(states.keys()))
    print(state)

    answer = input('What is the capitol of this state? ').title()
    if answer == states.get(state):
        print('correct')
        total_correct+=1
    else:
        print('wrong')
        total_wrong+=1
    del states[state]
print('You got',total_correct,'right and',total_wrong,'wrong')
