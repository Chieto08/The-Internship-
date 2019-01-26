list_of_numbers = []
numbers = input(" Enter the elements in the list and separate each by a comma: ")
list_of_numbers = numbers.split(",")
max_element = 0
for number in list_of_numbers:
    if int(number) > max_element:
        max_element = int(number)
print("The maximum element in the list is: ", max_element)
