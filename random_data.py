from random import randint
from pack_4bit_int import Int4

def generateData(amount):
    data = []
    for i in range (0,amount):
        data.append(Int4(randint(0,15)))
    return data[:]
