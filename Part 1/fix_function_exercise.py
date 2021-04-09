# Without adding any new lines of code, make count_dollar_signs work as intended
def count_dollar_signs(word):
    count = 0
    for char in word:
        if char == '$':
            count += 1
    return count
# make sure the return is outside of the loop otherwise the function will always return either 0 or 1


print(count_dollar_signs("$uper $ize"))
print(count_dollar_signs("$$$uper $$ize"))


def exponent(num=3, power=5):  # the values after the = are the default values
    return num ** power


print(exponent(2, 3))  # 8
print(exponent(5, 2))  # 25
print(exponent(4, 3))  # 64
print(exponent())  # 243
