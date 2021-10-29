string = 'Hello world!'
print(string.find('o'), string.rfind('o'))
new_string_list = string.split('o')
print(new_string_list)
final_string = ' '.join(new_string_list)
print(final_string)