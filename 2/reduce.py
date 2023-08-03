from functools import reduce

def concatenate_strings(strings):
    '''
    Concatenates the list of string to return single string

    Parameter:
        list(str) : takes in a list of strings

    Returns
        string: a single string containing concatenation of all the elements
    '''
    concat = reduce((lambda x, y: x + y), strings)
    return concat

print(concatenate_strings(['apple', 'banana', 'orange', 'kiwi', 'grape', 'pomegranate']))
    