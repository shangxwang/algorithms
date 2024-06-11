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

def merge_sort_inversion(array):
    """
    Compute pairs of inversions using merge sort
    :param array: a list of numbers
    :return: sorted list and number of inversions
    """
    if len(array) <= 1:
        return array, 0
    l, inv_l = merge_sort_inversion(array[:len(array)//2])
    r, inv_r = merge_sort_inversion(array[len(array)//2:])
    i = j = 0
    c = []
    inv = inv_l + inv_r
    print(l,r)
    while i < len(l) and j < len(r):
        if l[i] < r[j]:
            c.append(l[i])
            i += 1
        else:
            c.append(r[j])
            j += 1
            inv += len(l) - i
    c.extend(l[i:])
    c.extend(r[j:])
    return c, inv   