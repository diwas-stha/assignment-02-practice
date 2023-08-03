from functools import reduce

def concatenate_strings(strings):
    concat = reduce((lambda x, y: x + y), strings)
    return concat

print(concatenate_strings(['apple', 'banana', 'orange', 'kiwi', 'grape', 'pomegranate']))
    