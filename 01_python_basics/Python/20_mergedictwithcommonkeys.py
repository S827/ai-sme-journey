def merge_dicts_with_overlapping_keys(dicts):
    # Your code goes here
    
    dict = {}
    for item in dicts:
        # print(item)
        for it, v in item.items():
            # print(it)
            if it not in dict:
                dict[it] = v
            else:
                dict[it] += v
    return dict


print(merge_dicts_with_overlapping_keys([{'a': 1, 'b': 2}, {'b': 3, 'c': 4}, {'c': 5, 'd': 6}]))
print(merge_dicts_with_overlapping_keys([{'x': 10, 'y': 20}, {'y': 30, 'z': 40}, {'z': 50, 'x': 60}]))