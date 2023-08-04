'''
Given an array of strings (str), group the anagrams together. You can return the
answer in any order.
An Anagram is a word or phrase formed by rearranging the letters of a different
word or phrase, typically using all the original letters exactly once.

'''

from collections import defaultdict

def group_anagrams(strings):
    """
    Group anagrams together in the array of strings.

    Parameters:
        strings (list of str): The array of strings.

    Returns:
        list of list of str: A list containing lists of anagrams grouped together.
    """
    anagrams_dict = defaultdict(list)
    for string in strings:
        sorted_string = ''.join(sorted(string))
        anagrams_dict[sorted_string].append(string)

    return list(anagrams_dict.values())

input_strings = ["eat", "tea", "tan", "ate", "nat", "bat"]

print(group_anagrams(input_strings))