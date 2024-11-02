Python 3.10.6 (tags/v3.10.6:9c7b4bd, Aug  1 2022, 21:53:49) [MSC v.1932 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
#user input age
age = int(input('Enter your age: '))
Enter your age: 19
#output if age<=1 then infant
if age <= 1:
    print('You are an infant.')
#output if age>1 and age<13 then child
elif age > 1 and age < 13:
    print('You are a child.')
#output if age>=13 and age<20 then teenager
elif age >= 13 and age < 20:
    print('You are a teenager.')
#output if age>=20 then adult
else:
    print('You are an adult.')

    
You are a teenager.
