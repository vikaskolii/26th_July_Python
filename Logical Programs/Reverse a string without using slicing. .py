'Method 1: Using a for loop '''

def reverse_string(s):
        reversed_str = ""
        for char in s:
            reversed_str = char + reversed_str  # put current char in front
        return reversed_str


print(reverse_string("automation"))  # noitamotua

print("_____________________________________________")


' Method 2: Using recursion'
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

print(reverse_string("automation"))  # noitamotua