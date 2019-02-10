def Join_Lists_and_sort(list_A, list_B):
    concatenated_list = list_A + list_B
    print(merge_sort(concatenated_list))

def merge_sort(concatenated_list):
    if len(concatenated_list) > 1:
        mid = len(concatenated_list)//2
        left = concatenated_list[:mid]
        right = concatenated_list[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                concatenated_list[k] = left[i]
                i = i + 1
            else:
                concatenated_list[k] = right[j]
                j = j + 1
            k = k + 1

        while i < len(left):
            concatenated_list[k] = left[i]
            i = i + 1
            k = k+ 1
            
    return concatenated_list

Join_Lists_and_sort([1,2,5], [2,4,7])



            






    
    
