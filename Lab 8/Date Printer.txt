#user input date mm/dd/yyyy
initial_date = input('Enter a date in the mm/dd/yyyy format: ')
#remove / 
date_list = initial_date.split('/')
#convert mm to respective month
if date_list[0] == '01':
  print('January', end = ' ')
if date_list[0] == '02':
  print('February', end = ' ')
if date_list[0] == '03':
  print('March', end = ' ')
if date_list[0] == '04':
  print('April', end = ' ')
if date_list[0] == '05':
  print('May', end = ' ')
if date_list[0] == '06':
  print('June', end = ' ')
if date_list[0] == '07':
  print('July', end = ' ')
if date_list[0] == '08':
  print('August', end = ' ')
if date_list[0] == '09':
  print('September', end = ' ')
if date_list[0] == '10':
  print('October', end = ' ')
if date_list[0] == '11':
  print('November', end = ' ')
if date_list[0] == '12':
  print('December', end = ' ')
if int(date_list[0]) > 12:
  print('Enter the month in mm format.')

if int(date_list[1]) > 32:
  print('A month can have a maximum of 31 days. Reenter the date.')
#output date
print(date_list[1] + ', ' + date_list[2])
