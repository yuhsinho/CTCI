"""
ch1.1

Algorithm below is O(n) since lookup operation in sets is ammortized O(1)
and we must look at each character one time.
"""

def is_unique_string(string: str) -> bool:
    """
    If all characters in the string are different,
    then return True. Otherwise return False.
    """
    s = set()
    for c in string:
        if c in s:
            return False
        
        s.add(c)
    return True

def test_unique_string():
    print("Testing unique string")
    cases = [('abc', True), ('dbaa', False), ('', True)]
    for case in cases:
        assert is_unique_string(case[0]) == case[1]
    print("all tests passed")

"""
ch1.1

If we can't use additional data structure, there are two ways to implement.
One way is O(n^2).
"""

def is_unique_string_method2(string: str) -> bool:
    """
    Loop through each character,
    compare each character with the characters before itself.
    If all characters are different, return True. Otherwise False.
    """
    for i in range(len(string)):
        current_char = string[i]
        #print(current_char)
        for j in range(i):
            #print("Checking", string[j], "against", current_char)
            if (current_char == string[j]):
                return False
    return True

"""
ch1.2

In worst case, we have to check each character in a string, so it should be O(n).
"""
def check_permutation(string1: str, string2: str) -> bool:
    """
    If one string is a permuation of the other, return True. Otherwise False.
    """    
    """
    Method 1
    - Count the letter of each string and convert to a dictionary.
    - Check if two dictionaries are the same
    """
    #d1 = letter_count(string1)
    #d2 = letter_count(string2)
    #return compare_dictionaries(d1, d2)

    """
    Method 2
    - Count the letter of the first string and convert to a dictionary.
    - Loop through the second string and substract the count of the letter.
    - Check if the character in the second string is not in the dictionary
    - Check if the dictionary key value is equal to zero at the end.
    """
    d = letter_count(string1)
    for c in string2:
        if c not in d:
            return False
        else:
            d[c] = d.get(c, 0) - 1
    return all(value == 0 for value in d.values())

def letter_count(string: str):
    d = {}
    for c in string:
        d[c] = d.get(c, 0) + 1
    return d

def compare_dictionaries(d1: dict, d2: dict) ->bool:
    if (d1 == d2):
        return True
    return False
    

def test_check_permutation():
    print("Testing unique string")
    cases = [(('abc', 'bca'), True), (('aabc','bbac'), False), (('abc','abcd'), False)]
    for case in cases:
        assert check_permutation(case[0][0], case[0][1]) == case[1]
    print("all tests passed")
        


def main():
    """ch1.1"""
    #test_unique_string()
    #print(is_unique_string_method2('dbgaa'))
    """ch1.2"""
    test_check_permutation()
    
    

if __name__== '__main__':
    main()
