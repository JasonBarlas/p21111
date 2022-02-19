import json

give_me_your_file = "./textfile_samples/sample_dictionary.txt"             #<-- Give the path to your file.

def list_keys(temp_dict):
	temp_list = []
	for key in temp_dict.keys():
		temp_list.append(key)
	return temp_list

with open(give_me_your_file, "r") as file:
    dictionary_list = [json.loads(i) for i in file.readlines()]


print("--------------------------------------------------------------------------------------------")
green_card_1 = True
for j in range(0, len(dictionary_list)-1):
    if list_keys(dictionary_list[j]) != list_keys(dictionary_list[j+1]):
        green_card_1 = False

green_card_2 = False
key_index = 0               #<-- This one was never used.
if green_card_1 == True:
    print("List Of Available Keys: ", list_keys(dictionary_list[0]))
    user_selection = input("Please Select A Key From Those Listed (by typing its name): ")
    for j in list_keys(dictionary_list[0]):
        if j == user_selection:
            green_card_2 = True
        if green_card_2 == False:
            key_index += 1

user_selection_check = True
if green_card_1 == True:
    if green_card_2 == True:
        print("Your Selected Key: " + user_selection)
    else:
        print("The Key You Selected Was Not Found.")
        user_selection_check = False
        green_card_1 = False


if green_card_1 == True:

    values_by_key_list = []
    for j in dictionary_list:
        values_by_key_list.append(j[user_selection])

    most_common_value = []
    results_most_common = []
    max_most_common = -1

    green_card_2 = True
    for j in range(0, len(values_by_key_list)-1):
        if type(values_by_key_list[j]) != type(values_by_key_list[j+1]):
            green_card_2 = False

    if green_card_2 == True:
        min_value = values_by_key_list[0]
        max_value = values_by_key_list[0]
        min_value_counter = 0
        max_value_counter = 0

    for j in values_by_key_list:

        if green_card_2 == True:
            if j >= max_value:
                if j == max_value:
                    max_value_counter += 1
                if j > max_value:
                    max_value_counter = 1
                max_value = j

            if j <= min_value:
                if j == min_value:
                    min_value_counter += 1
                if j < min_value:
                    min_value_counter = 1
                min_value = j

        value_counter = -1
        for j_2 in values_by_key_list:
            if j == j_2:
                value_counter += 1
        most_common_value.append(value_counter)


    for j in most_common_value:
        if j >= max_most_common:
            max_most_common = j
    j_2 = 0
    for j in most_common_value:
        if j == max_most_common:
            check_green_card = True
            for j_3 in results_most_common:
                if j_3 == values_by_key_list[j_2]:
                    check_green_card = False
            if check_green_card == True:
                results_most_common.append(values_by_key_list[j_2])
        j_2 += 1
    check_green_card = False
    for j in most_common_value:
        if j != most_common_value[0]:
            check_green_card = True
    if check_green_card == True:
        print("Most Common Values Of Your Selected Key: ", results_most_common)
    else:
        print("All Values Of Your Selected Key Are Equally Common.")


    if green_card_2 == True:
        print("Maximum Value: ", max_value, " (appeared: ", max_value_counter, " times.)")
        print("Minimum Value: ", min_value, " (appeared: ", min_value_counter, " times.)")
    else:
        print("The Values Of Your Selected Key Are Not Comparable.")

if (green_card_1 == False) and (user_selection_check == True):
    print("Given Dictionaries Have Different Keys.")
print("--------------------------------------------------------------------------------------------")