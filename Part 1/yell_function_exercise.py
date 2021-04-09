# Implement a function called yell  which accepts a single string argument.
# It should return(not print) an uppercased version of the string with an exclamation point aded at the end.  For example:
# yell("go away")   # "GO AWAY!"
# yell("leave me alone")   # "LEAVE ME ALONE!"

def yell(word):
    return word.upper() + "!"


print(yell("Testing"))

# Using f-strings


def yell(word):
    return f"{word.upper()}!"
