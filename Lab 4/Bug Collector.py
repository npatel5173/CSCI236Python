#running total of number of bugs collected
total = 0
#for loop for 5 days
for num in range(1, 6):
  print('Enter number of bugs collected for day', num )
  #ask number of bugs collected for each day
  num_of_bugs = int(input('Enter a number: '))
  total += num_of_bugs
#when loop finished, display total bugs collected
print('You have collected a total of', total , 'bugs.')







