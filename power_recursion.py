import time
import math


def power(a, b):
    s = 1
    for i in range(b):
        power.counter += 1
        s *= a
    return s


def power2(x, y):
    power2.counter += 1
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return (x*power(x, y-1))


def power3(i, j):
    power3.counter += 1
    if j == 0:
        return 1

    elif j == 1:
        return i

    elif j % 2 == 0:
        i **= 2
        return power3(i, j//2)
    else:
        return i*power3(i, j-1)


def power4(n, m):
    power4.counter += 1
    return n**m


# def power5(n, m):
#     power5.counter += 1
#     return math.pow(n, m)


base = 2
exponent = 1000000

power.counter = 0
time1 = time.time()
a = power(base, exponent)
time2 = time.time()
print('power use :', time2-time1)
print('power used :', power.counter)

power2.counter = 0
time1 = time.time()
b = power2(base, exponent)
time2 = time.time()
print('power2 use :', time2-time1)
print('power used :', power2.counter)

power3.counter = 0
time1 = time.time()
c = power3(base, exponent)
time2 = time.time()
print('power3 use :', time2-time1)
print('power used :', power3.counter)

power4.counter = 0
time1 = time.time()
d = power4(base, exponent)
time2 = time.time()
print('power4 use :', time2-time1)
print('power used :', power4.counter)

# power5.counter = 0
# time1 = time.time()
# e = power5(base, exponent)
# time2 = time.time()
# print('power5 use :', time2-time1)
# print('power used :', power5.counter)

print(a == b == c == d)
