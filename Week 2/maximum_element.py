def maximum_element(list_of_numbers):
    max_element = 0
    for number in list_of_numbers:
        if int(number) > max_element:
            max_element = int(number)
    return "The maximum element in the list is: " + str(max_element)

print(maximum_element([1,22,878,3738,9]))

