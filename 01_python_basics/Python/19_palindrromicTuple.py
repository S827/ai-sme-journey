def is_palindromic_tuple(tup):
    # Your code goes here
    if not tup or len(tup) == 1:
        return True

    check = False
    for i in range(len(tup)//2):
        if tup[i] == tup[-i-1]:
            check = True
        else:
            check = False
    return check


print(is_palindromic_tuple((1, 2, 3, 2, 1,1)))
print(is_palindromic_tuple(('a', 'b', 'c', 'c', 'b', 'a')))
print(is_palindromic_tuple(()))
print(is_palindromic_tuple(('a')))