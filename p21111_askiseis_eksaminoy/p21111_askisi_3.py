import string

give_me_your_file = "./textfile_samples/two_cities_ascii.txt"        #<-- Give the path to your file.


with open(give_me_your_file, "r") as text_file:

  text_file_contents = text_file.read()
  for char in string.printable:
      if char not in string.ascii_letters:
        text_file_contents = text_file_contents.replace(char, " ")
  words_list = text_file_contents.split()

default_char_sum = 20       #<-- You may change this one to any positive integer value or zero.
enable_user_input = False        #<-- Change this to True to enable user inputs.
if enable_user_input == True:
  print("--------------------------")
  user_input = input("Give Character Sum: ")
  no_int = False
  for char in user_input:
    if char not in string.digits:
      no_int = True
  if no_int == False:
    char_sum = int(user_input)
  else:
    print("User Input Error.")
    char_sum = default_char_sum
else:
  char_sum = default_char_sum

word_remove = []
word_remove_pos = []
i=0
while i < len(words_list):
  if i != len(words_list) - 1:
    if len(words_list[i]) + len(words_list[i+1]) == char_sum:
      word_remove.append(words_list[i])
      word_remove.append(words_list[i+1])
      word_remove_pos.append(i)
      word_remove_pos.append(i+1)
      i+=1
  i+=1

j=0
for i in word_remove_pos:
  if word_remove[0] == words_list[i-j]:
    words_list.pop(i-j)
    word_remove.pop(0)
    j+=1

print("----------------------------------------------------------------------------------------------------------")
print("After 1 Scan: Removed ", j//2," Pairs Of Consecutive Words With ", char_sum, " As The Sum Of Their Characters.")
print("----------------------------------------------------------------------------------------------------------")


check_length = []
count_length = []
for i in words_list:
  if len(i) not in check_length:
    check_length.append(len(i))
    count_length.append(1)
  else:
    for j in range(0, len(check_length)):
      if len(i) == check_length[j]:
        count_length[j] += 1

for i in range(0, len(check_length)):
  for j in range(len(check_length)-1, i,-1):
    if check_length[j] < check_length[j-1]:
      temp_value = check_length[j]
      check_length[j] = check_length[j-1]
      check_length[j-1] = temp_value
  print("Total number of words with ", check_length[i], " letters:", count_length[i])
print("----------------------------------------------------------------------------------------------------------")