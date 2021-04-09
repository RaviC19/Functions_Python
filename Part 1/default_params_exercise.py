# Write a function called speak  that accepts a single parameter, animal.
# If animal is "pig", it should return "oink".
# If animal is "duck", it should return "quack".
# If animal is "cat", it should return "meow"
# If animal is "dog", it should return "woof"
# If animal is anything else, it should return "?"
# If no animal is specified, it should default to "dog"

def speak(animal="dog"):
    if animal == "pig":
        return "oink"
    elif animal == "duck":
        return "quack"
    elif animal == "cat":
        return "meow"
    elif animal == "dog":
        return "woof"
    return "?"


print(speak("dog"))
print(speak("cat"))
print(speak("elephant"))
print(speak("pig"))
print(speak())

# Shorter version involves a dictionary that maps animal names to noises
# We use the dictionary.get() method to retrieve the correct animal noise and save it to a variable called noise
# .get() will return None  if the animal is not in the dictionary.  Then we just check to see if noise  exists.  If it does, return noise .  Otherwise, return "?"

noises = {
    "dog": "woof",
    "pig": "oink",
    "duck": "quack",
    "cat": "meow"
}


def speak(animal="dog"):
    noises = {"dog": "woof", "pig": "oink", "duck": "quack", "cat": "meow"}
    noise = noises.get(animal)
    if noise:
        return noise
    return "?"

# even more compact version which passes a default value to get()


def speak(animal='dog'):
    noises = {'pig': 'oink', 'duck': 'quack', 'cat': 'meow', 'dog': 'woof'}
    return noises.get(animal, '?')
