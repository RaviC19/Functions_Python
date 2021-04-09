# Write a function called last_element which takes in one parameter (a list) and returns the last value in the list
# It should return None if the list is empty

def last_element(value_list):
    if len(value_list) == 0:
        return None
    return value_list.pop(-1)


print(last_element([1, 2, 3, 4, 5]))
print(last_element(["a", "b", "c", "d"]))
print(last_element([]))

# First check to see if the list exists (if it has data in it).  If it does, return the -1 item (last item).  Otherwise, return None.


def last_element(l):
    if l:
        return l[-1]
    return None
