#recursive function that print 1 - n
def message(times):
  if times > 0:
    message(times - 1)
    print(times)
#user input int argument, n    
n = int(input('Enter a number: '))
message(n)
