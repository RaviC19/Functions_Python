# Write a function called return_day. this function takes in one parameter (a number from 1-7) and returns the day of the week (1 is Sunday, 2 is Monday, 3 is Tuesday etc.)
# If the number is less than 1 or greater than 7, the function should return None
# Hint: store the days of the week in a list (or dict using numbers as keys).

def return_day(number):
    days = {1: "Sunday", 2: "Monday", 3: "Tuesday",
            4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}
    return days.get(number)


print(return_day(1))
print(return_day(5))
print(return_day(9))
print(return_day(-3))

# This solution: keeps track of the days in a list, checks to make sure num isn't <0 or >6, returns the corresponding day
# Use days[num-1] because return_day(1) should return 0th item in list.


def return_day(num):
    days = ["Sunday", "Monday", "Tuesday",
            "Wednesday", "Thursday", "Friday", "Saturday"]
    # Check to see if num valid
    if num > 0 and num <= len(days):
        # use num - 1 because lists start at 0
        return days[num-1]
    return None

# Advanced solution that involves error handling. It eliminates the need to check to see if num is a valid index in the list


def return_day(num):
    try:
        return ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"][num-1]
    except IndexError as e:
        return None
