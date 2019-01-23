user_number = int(input(" Enter a number here to calculate the sum of the \n numbers from 1 to your chosen number: "))
total_sum = 0
for number in range(1, user_number + 1):
    if number%3 == 0 or number%5 == 0:
        total_sum = total_sum + number
print(total_sum)
    
