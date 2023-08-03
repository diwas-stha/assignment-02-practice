"""
[filter] Write a Python function filter_long_strings that takes a list of strings as
input and uses the filter function to return a new list containing strings with more
than 5 characters.

"""

def filter_long_strings(strings):
    """
        Filter the strings with more than 5 characters from the input list.

        Parameters:
            (list of str): The list of strings.

    """

    filtered_list = list(filter(lambda string: len(string)>5, strings))
    return filtered_list

print(filter_long_strings(['apple', 'banana', 'orange', 'kiwi', 'grape', 'pomegranate']))  
# Output: ['banana', 'orange', 'pomegranate']

print(filter_long_strings(['hello', 'world', 'Python', 'is', 'awesome', 'Javascript']))  
# Output: ['Python', 'awesome', 'Javascript']
 