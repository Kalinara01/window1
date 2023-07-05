import math
name_of_list = ["tree"]
string = name_of_list[0]
first_half = string[0:math.ceil(len(string)/2)]
second_half = string[int(len(string)/2):]
new_list = list(second_half+first_half)
print(first_half,second_half)
print(new_list)
