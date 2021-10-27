
exercise = input('Enter your exercise: ')
list_exercise = exercise.split('=')
if len(list_exercise) == 2:
    print(list_exercise)
    if eval(list_exercise[0]) == eval(list_exercise[1]):
        print('True')
    else:
        print('False')
else :
    print('Invalid exercise')
