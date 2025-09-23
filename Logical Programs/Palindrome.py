def is_palindrome(s):
    return s == s[::-1]

print(is_palindrome("madam"))   # True
print(is_palindrome("test"))    # False


# s[::-1] → this makes a reversed copy of the string (just like we explained before).
# "madam"[::-1] → "madam"
# "test"[::-1] → "tset"
#
# s == s[::-1] → compares original string with its reversed version.
# If both are same → return True (it is a palindrome).
# If they are different → return False.





