Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#get prices of 5 purchasing items
price_1 = float(input('Enter the price of the 1st item: '))
Enter the price of the 1st item: 3.69
price_2 = float(input('Enter the price of the 2nd item: '))
Enter the price of the 2nd item: 4.29
price_3 = float(input('Enter the price of the 3rd item: '))
Enter the price of the 3rd item: 2.89
price_4 = float(input('Enter the price of the 4th item: '))
Enter the price of the 4th item: 5.39
price_5 = float(input('Enter the price of the 5th item: '))
Enter the price of the 5th item: 7.49
#get subtotal
subtotal = price_1 + price_2 + price_3 + price_4 + price_5
#display subtotal
print(subtotal)
23.75
#assign sales tax
sales_tax = 0.07
#display sales tax
print(sales_tax)
0.07
#find total
total = (subtotal * sales_tax) + subtotal
#display total
print(total)
25.4125
print(format(total, '.2f'))
25.41
