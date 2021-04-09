from random import random


def flip_coin():
    if random() > 0.5:
        return ("You flipped Heads")
    else:
        return ("You flipped Tails")


print(flip_coin())


def speak_pig():
    return "oink"


print(speak_pig())
