# feel free to use these dictionaries in your solution!
str_to_num = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9, "ten": 10}
num_to_str = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten"}

def add_str_nums(num_1, num_2):
    # convert the string numbers to ints so Python can perform math
	if num_1 in str_to_num:
	    val_1 = str_to_num[num_1]
	else:
	    val_1 = 0
	if num_2 in str_to_num:
	    val_2 = str_to_num[num_2]
	else:
	    val_2 = 0
	# add the values, now that they're ints
	sum_val = val_1 + val_2
	# convert the value back to a string
	if sum_val in num_to_str:
	    return num_to_str[sum_val]
	else:
	    return "greater than ten"

# Input handling (do not edit)
parts = input().split(" ")
print(add_str_nums(parts[0], parts[1]))

##########################################################################################################

Write a function that adds two number strings (i.e., "one" + "three" = "four").

Parameters
num_1: a string that represents a number (i.e., "four" is 4).
num_2: a string that represents a number (i.e., "four" is 4).

Output
Returns the string that represents the sum of num_1 + num_2

Edge cases

    If num_1 or num_2 is greater than "ten", it should instead become "zero". If the sum of num_1 + num_2 is greater than "ten", it should instead become "greater than ten" 

STDIN format
num_1 num_2 (for instance, one three)

Sample input / outputs
one three / four
zero five / five
six four / ten
six eleven / six
eleven eleven / zero
seven four / greater than ten
