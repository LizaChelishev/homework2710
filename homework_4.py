#list = ['liza', 'is', 'studying', 'python']
#for i in range (0, len(list)+1):


class1 = ['david', 'yosi' ,'ruti']
class2 = ['liza' , 'may']
class3 = ['yuval' , 'adi' , 'aviv', 'gfg']

bet1 = ['davidb', 'yosib' ,'rutib']
bet2 = ['lizab' , 'mayb']


layer_alef = [class1 , class2 , class3]
layer_bet = [bet1 , bet2]

school = [layer_alef, layer_bet]
# school is list of list of list of string
for layer in school:
    print('New layer')
    for kita in layer:
        print('New kita')
        for pupil in kita:
            print('The pupil name is: ', pupil)








