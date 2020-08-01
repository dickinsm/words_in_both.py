# Author: Makaliah Dickinson
# Date: 8/1/2020
# Description: Write a function named that takes two strings as parameters and returns a set of the words
#              contained in both strings.

def words_in_both(s1, s2):
    words1 = s1.lower().split(" ")
    words2 = s2.lower().split(" ")
    result = []
    for x in words1:
        if (x in words2) and (x not in result):
            result.append(x)
    return set(result)
sentence='Not the comfy chair!'
print(sentence.split())
['Not','the','comfy','chair!']