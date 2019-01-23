user_number = int(input(" Enter a number here to calculate the sum of the \n numbers from 1 to your chosen number: "))
total_sum = 0
while user_number > 0:
    total_sum = total_sum + user_number
    user_number = user_number - 1
print(total_sum)
    
