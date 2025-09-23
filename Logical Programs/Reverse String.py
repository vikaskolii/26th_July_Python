def reverse_string(s):
    return s[::-1]                   #tells Python → “Start from the end, go backwards, and collect everything.”

print(reverse_string("automation"))  # noitamotua
print(reverse_string("vikas"))       #sakiv


# s[::-1] is slicing in Python.
# Normally, s[start:end:step]
# start = where to begin
# end = where to stop
# step= how many steps to jump (1 means forward, -1 means backward).
#
# When we write s[::-1]
# No start → it starts from the end of the string.
# No end → it goes till the beginning.
# -1 step → moves backward one by one.
# So, "automation"[::-1] reads the string from last letter to first letter → "noitamotua".
#So, "vikas"[::-1] reads the string from last letter to first letter → "sakiv".
