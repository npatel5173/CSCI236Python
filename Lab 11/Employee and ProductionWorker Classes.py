class Employee:
  #Employee class with attributes for Employee name and Employee Number
  def __init__(self, name, number):
    self.__name = name
    self.__number = number
  #Mutators methods for Employee class
  def set_name(self, name):
    self.__name = name
  def set_number(self, number):
    self.__number = number
  #Accessor methods for Employee clas
  def get_name(self):
    return self.__name
  def get_number(self):
    return self.__number
#ProductionWorker subclass of Employee class with attributes for Shift Number (an int) and Hourly pay rate
class ProductionWorker(Employee):
  def __init__(self, shiftNumber, hourlyPayRate):
    self.__shiftNumber = shiftNumber
    self.__hourlyPayRate  = hourlyPayRate
  #Mutators methods for ProductionWorker subclass
  def set_shiftNumber(self, shiftNumber):
    self.__shiftNumber = shiftNumber
  def set_hourlyPayRate(self, hourlyPayRate):
    self.__hourlyPayRate = hourlyPayRate
  #Accessor methods for ProductionWorker subclass
  def get_shiftNumber(self):
    return self.__shiftNumber
  def get_hourlyPayRate(self):
    return self.__hourlyPayRate
   
#user input object's data attributes
#store data in object
name = input('Enter your name: ')
number = int(input('Enter your employee number: '))
#day shift = 1
#night shift = 2
shiftNumber = int(input('Enter your shift number (1 for day shift and 2 for night shift): '))
hourlyPayRate = float(input('Enter your hourly pay rate: '))

#use accessor method and display data on screen
print('Your name is ' + name)
print('Your Employee number is ' + str(number))
if shiftNumber == 1:
  print('You work in a day shift.')
if shiftNumber == 2:
  print('You work in a night shift.')
elif shiftNumber >= 3:
  print('Refresh the page and reenter a valid shift number.')
print('Your hourly pay rate is $' + str(hourlyPayRate))
