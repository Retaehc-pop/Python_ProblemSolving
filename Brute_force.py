from itertools import product
import string

charset = string.printable
n = 1
while True:
    for i in product(charset, repeat=n):
        print(''.join(i))
    n += 1
