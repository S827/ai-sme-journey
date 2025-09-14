def merge_lists_to_dictionary(keys, values):
    # Your code goes here
    if not keys or not values:
        return {}
    if len(keys) != len(values):
        return False
    dict = {}
    for i in range(len(values)):
            dict[keys[i]] = values[i]        
    return dict



keys = ['key1', 'key2']
values = [100, 200, 300]
print(merge_lists_to_dictionary(keys, values))
