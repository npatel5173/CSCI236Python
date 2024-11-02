#user input first, middle, last names
first_name = input('Enter your first name: ')
middle_name = input('Enter your middle name: ')
last_name = input('Enter your last name: ')
#get first letter of each string
#convert to uppercase
first_initial = first_name[0].upper()
middle_initial = middle_name[0].upper()
last_initial = last_name[0].upper()
#output initials
print(first_initial + '. ' + middle_initial + '. ' + last_initial)
