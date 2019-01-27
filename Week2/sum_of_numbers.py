def sum_of_numbers(user_number):
    total_sum = 0
    number = user_number
    while user_number > 0:
        total_sum = total_sum + user_number
        user_number = user_number - 1
    return "The total sum from 1 to " + str(number) + " is "+ str(total_sum)

print(sum_of_numbers(20))       
