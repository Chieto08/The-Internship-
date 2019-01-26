list_A = [1,2,5]
list_B = [2,4,7]
concatenated_list = []

def Join_Lists_and_sort():
    concatenated_list = list_A + list_B
    lenn = len(concatenated_list) - 1
    while lenn > 0:
        for item in range(lenn):
            if concatenated_list[item] > concatenated_list[item + 1]:
                temp = concatenated_list[item]
                concatenated_list[item] = concatenated_list[item + 1]
                concatenated_list[item + 1] = temp
        lenn = lenn - 1
    print(concatenated_list)

Join_Lists_and_sort()

            






    
    
