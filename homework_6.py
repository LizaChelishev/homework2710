my_full_name = 'Liza Chelishev'
print(my_full_name[-5:len(my_full_name)])
print(my_full_name[0:len(my_full_name)//3])
print(my_full_name.count('a'))
print(my_full_name.count('b') > 0)
list_full_name = my_full_name.split()
print(list_full_name)
list_full_name.reverse()
print(list_full_name)
last_name = list_full_name[0].upper()
print(last_name)
first_name = list_full_name[1].replace('i',"")
print(first_name)
print(last_name + ' ' + first_name)