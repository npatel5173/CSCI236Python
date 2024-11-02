Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#ask user for num range 1-7
num = int(input('Enter any number from 1 through 7: '))
Enter any number from 1 through 7: 5
#output num with corresponding day of the week
if num == 1:
    print('The 1st day of the week is Monday.')
elif num == 2:
    print('The 2nd day of the week is Tuesday.')
elif num == 3:
    print('The 3rd day of the week is Wednesday.')
elif num == 4:
    print('The 4th day of the week is Thursday.')
elif num == 5:
    print('The 5th day of the week is Friday.')
elif num == 6:
    print('The 6th day of the week is Saturday.')
elif num == 7:
    print('The 7th day of the week is Sunday.')
#output error message if num is outside of range
else:
    print('This number is outside the range of 1 through 7. Please try again.')

    
The 5th day of the week is Friday.
