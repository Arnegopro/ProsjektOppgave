from random import randint
from pack_4bit_int import Int4

x = Int4(randint(0,15))
y = Int4(randint(0,15))

print(x, y)
print(x + y)
print(x - y)
print(x/y)
print(x*y)
