#user input store sales for each day of the week
sales = []
monday_sale = input('Enter the total sales for Monday: ')
tuesday_sale = input('Enter the total sales for Tuesday: ')
wednesday_sale = input('Enter the total sales for Wednesday: ')
thursday_sale = input('Enter the total sales for Thursday: ')
friday_sale = input('Enter the total sales for Friday: ')
saturday_sale = input('Enter the total sales for Saturday: ')
sunday_sale = input('Enter the total sales for Sunday: ')
#store sales in a list
sales.append(monday_sale)
sales.append(tuesday_sale)
sales.append(wednesday_sale)
sales.append(thursday_sale)
sales.append(friday_sale)
sales.append(saturday_sale)
sales.append(sunday_sale)
#calculate total sales for the week using for loop
total_sales = 0
for value in sales:
  total_sales += float(value)
print('Your total sales for the week is $', format(total_sales, ',.2f'), sep = '')

