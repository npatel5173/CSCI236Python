#read contents of a text file
#display the frequency of each word
dictionary = dict()
input_file = open('words.txt', 'r')
content = input_file.read()
word_list = content.split()
for split in word_list:
  if split not in dictionary:
    dictionary[split] = split
for key in dictionary:
  print(key, word_list.count(dictionary[key]))
