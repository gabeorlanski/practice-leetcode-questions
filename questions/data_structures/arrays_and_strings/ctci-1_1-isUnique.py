"""
Given a string `s`, return if it is entirely unique characters
"""


from collections import Counter
def isUnique(s):
    # Since a string is an iterable, you can put it into a Counter and get the counts of each character in the string. It probably could be better optimized
    char_counts = Counter(s)
    
    # Return true if none of the characters have a count > 1. If they do, then it is not a unique character in the string.
    return not any(c>1 for c in char_counts.values()) 

def isUniquePart2(s):
    # initialize the previous character variable to None
    prev_char = None
    
    # `s` is an iterable of characters, therefore you can sort it. We sort the string `s` then iterate over it. Since it is sorted, we know that if any character is equal to the previous character, it is not a unique character in the string. 
    for c in sorted(s):
        # Check if `prev_char` has been set to a character. If it has, check if it is equal to the current. If it has, it is not unique, and we return False.
        if prev_char and prev_char == c:
            return False

        # Set the previous char to the current char.
        prev_char = c
    return True

if __name__ == "__main__":
    
    # Create the tests, they are in the form (input, output)
    tests = [
        ("abcd",True),
        ("aabcd",False),
        ("Aabcd",True),
        ("",True)
    ]

    for input_val, expected in tests:
        print(f"Input of '{input_val}' should be {expected}")
        assert isUnique(input_val) == expected
        assert isUniquePart2(input_val) == expected
        