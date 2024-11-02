class Pet:
  #data attributes: name, animal type, and age
  #init method to create attributes
  def __init__(self, name, animal_type, age):
    self.__name = name
    self.__animal_type = animal_type
    self.__age = age

  #methods: set_name, set_amimal_type, set_age, get_name, get_animal_type, and get_age
  def set_name(self, name):
    self.__name = name

  def set_animal_type(self, animal_type):
    self.__animal_type = animal_type

  def set_age(self, age):
    self.__age = age

  def get_name(self):
    return self.__name

  def get_animal_type(self):
    return self.__animal_type

  def get_age(self):
    return self.__age

#user input the name, type and age of pet and store data as object's attributes
input_name = input("Enter your pet's name: ")
input_animal_type = input("Enter the type of pet you have: ")
input_age = input("Enter your pet's age: ")
#retrieve pet's name, type and age and display data on screen
retrieve = Pet(input_name, input_animal_type, input_age)
name = retrieve.get_name()
animal_type = retrieve.get_animal_type()
age = retrieve.get_age()
print("Your pet's name is " + name + ".")
print("Your pet is a " + animal_type + ".")
print("Your pet's age is " + age + ".")
