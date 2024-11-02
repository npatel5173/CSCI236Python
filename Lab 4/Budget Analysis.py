#user input amount budgeted for a month
budget = float(input('Enter the amount budgeted for a month: '))
while budget < 0:
  print('The budget amount cannot be negative.')
  budget = float(input('Enter the correct budget amount: '))
print('Enter each of your expense values for a month.')
#keep a running total
total = 0.00
#variable to control the loop
another_expense = 'y'
#while loop for each expense for the month
while another_expense == 'y':
  expense = float(input('Enter a value: '))
  while expense < 0: 
    print('The expense value cannot be negative.')
    expense = float(input('Enter the correct value: '))
  total += expense
  another_expense = input('Do you have to add another expense value? Enter y for yes: ')
print('You have spent $', format(total, ',.2f'))
#when loop finishes, display the amount that user is over or under budget
if(total < budget):
  under_budget_value = budget - total
  print('You are under budget by $', format(under_budget_value, ',.2f'))
elif (total > budget):
  over_budget_value = total - budget
  print('You are over budget by $', format(over_budget_value, ',.2f'))
else:
  print('You have spent all of your budgeted value.')
