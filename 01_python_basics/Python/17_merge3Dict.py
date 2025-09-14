def merge_three_dictionaries(dict1, dict2, dict3):
    # Your code goes here
    return {**dict1, **dict2, **dict3}

print(merge_three_dictionaries({'a': 1, 'b': 2}, {'c': 3, 'd': 4}, {'e': 5, 'f': 6}))