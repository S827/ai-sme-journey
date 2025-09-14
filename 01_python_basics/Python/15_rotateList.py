def rotate_list(lst, k):
    # Your code goes here
    if not lst:
        return []
    lst_copy = lst.copy()
    max_index = len(lst) - 1
    j = 0
    k = k % len(lst)
    for i in range(len(lst)):
        if i+k <= max_index:
            lst_copy[i+k] = lst[i]
        else:
            lst_copy[j] = lst[i]
            j += 1
        print(lst_copy)
    return lst_copy

print(rotate_list([1,2,3,4,5], 5))