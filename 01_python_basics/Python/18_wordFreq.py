def count_word_frequency(sentence):
    # Your code goes here
    dict = {}
    words = sentence.split(' ')
    if not sentence:
        return {}
    for word in words:
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    return dict

print(count_word_frequency("hello world hello"))
print(count_word_frequency("the quick brown fox jumps over the lazy dog"))
print(count_word_frequency(''))