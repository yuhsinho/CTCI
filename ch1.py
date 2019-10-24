"""
ch1.1

Algorithm below is O(n) since lookup operation in sets is ammortized O(1)
and we must look at each character one time.
"""

def is_unique_string(string: str) -> bool:
    """
    if all characters in the string are different then
    return True. Otherwise return False.
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

If we can't use data structure,
one way to implement this is O(n^2).
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



def main():
    test_unique_string()
    #print(is_unique_string_method2('dbgaa'))

if __name__== '__main__':
    main()
