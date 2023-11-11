# Bryan Ulloa
# 11/11/23

#  Write a Python function that takes a list of numbers and returns a new list with unique elements of the first list.  Use list [1, 3, 3, 3, 6, 2, 3, 5]. Use the append function.

def unique_elements(input_list):
    return list(set(input_list))

my_list = [1, 3, 3, 3, 6, 2, 3, 5]
list.append
result = unique_elements(my_list)
print("The list with unique elements is:", result)
