num_content = int(input('How many file data do you want to add in the file? '))
search_file = input('Enter a filename: ')
open_file = open(search_file, 'w')
for data in range(1, num_content + 1):
  content = input('Enter file data #' + str(data) + ': ')
  open_file.write(content + '\n')
  print(str(data) + ': ' + content)
open_file.close()
