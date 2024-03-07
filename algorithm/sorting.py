def insertion_sort(array):
    """
    Sort array in increasing order using insertion sort
    :param array: a list of numbers
    :return: sorted list
    """
    for i in range(1, len(array)): #iterate through the second to the last element of the list.
        key = array[i] 
        left = i - 1
        while key < array[left] and left >= 0: #if the current key is smaller than the previous element, swap them.
            array[left + 1] = array[left] 
            left -= 1 
        array[left + 1] = key
    return array

def merge_sort(array):
    """
    Sort array in increasing order using merge sort
    :param array: a list of numbers
    :return: sorted list
    """
    if len(array) <= 1: 
        return array
    left = merge_sort(array[:len(array)//2]) 
    right = merge_sort(array[len(array)//2:])
    i = j = 0
    result = [] #new list to append sorted items
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:]) #append the rest to the result array
    result.extend(right[j:])
    return result