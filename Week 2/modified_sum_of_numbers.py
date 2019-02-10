def sum_of_numbers(user_number):
    total_sum = 0
    for number in range(1, user_number + 1):
        if number%3 == 0 or number%5 == 0:
            total_sum = total_sum + number
    return "The sum of numbers from 1 is : " + str(total_sum)
        
print(sum_of_numbers(400))
