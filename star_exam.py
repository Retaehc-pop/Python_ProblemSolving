def clear():
    print("\n")
    print("-"*30)
    print("\n")


n = int(input())

# xxxxx
for i in range(n):
    print("X", end="")
clear()
"""
X
X
X
X
X
"""
for i in range(n):
    print("X")
clear()

# square
for i in range(n):
    for j in range(n):
        print("X", end="")
    print()
clear()

# triangle
for i in range(n):
    for j in range(i+1):
        print("X", end="")
    print()

clear()

for i in range(n):
    print("X" * (i+1))
clear()

# reverse triangle
for i in range(n, 0, -1):
    for j in range(i):
        print("X", end="")
    print()
clear()

# square + triangle
for i in range(n):
    for j in range(n):
        print("X", end="")
    for k in range(i+1):
        print("X", end="")
    print()
clear()
# reverse flip triangle
for i in range(n):
    print("-" * i, end="")
    for j in range(n - i):
        print("X", end="")
    print()
clear()

# backslash
for i in range(n):
    print("-" * i, end="")
    print("X")
clear()

# slash
for i in range(n, 0, -1):
    for j in range(i):
        print("-", end="")
    print("X", end="")
    print()
clear()
# triangle 2n+1
for i in range(n):
    for j in range(n-i):
        print("-", end="")
    for k in range(2*i+1):
        print("X", end="")
    print()
clear()

# 2 tower
for i in range(n):
    for j in range(n-i):
        print("X", end="")
    for k in range(2*i+1):
        print("-", end="")
    for l in range(n-i):
        print("X", end="")
    print()
clear()
# triangle 2n+1 reverse
for i in range(n, 0, -1):
    for j in range(n-i):
        print("-", end="")
    for k in range(2*i-1):
        print("X", end="")
    print()
clear()
# diamon
for i in range(n):
    for j in range(n-i):
        print("-", end="")
    print("X", end="")
    for k in range(2*i+1):
        print("-", end="")
    print("X", end="")
    print()
print("X"+((2*n)+1)*"-"+"X")
for i in range(n):
    for j in range(i+1):
        print("-", end="")
    print("X", end="")
    for k in range(2*(n-i)-1):
        print("-", end="")
    print("X", end="")
    print()
clear()
# x
for i in range(n):
    for j in range(i):
        print("-", end="")
    print("X", end="")
    for k in range(2*(n-i)-1):
        print("-", end="")
    print("X", end="")
    print()
print("-"*n+"X")
for i in range(n):
    for j in range(n-i-1):
        print("-", end="")
    print("X", end="")
    for k in range(2*i+1):
        print("-", end="")
    print("X")
clear()

# Y
for i in range(n):
    for j in range(i):
        print("-", end="")
    print("X", end="")
    for k in range(2*(n-i)-1):
        print("-", end="")
    print("X", end="")
    print()
for i in range(n):
    for j in range(n):
        print(" ", end="")
    print("X")
clear()
# Z
print("X"*(n+1), end="")
print()
for i in range(n-1):
    for j in range(n-i):
        print("-", end="")
    print("X")
print("X"*(n+1), end="")
clear()

# box corner
for i in range(n):
    for j in range(n):
        print("-", end='')
    for k in range(n-i):
        print("-", end='')
    print("X")
print("x"*(n+1))
for i in range(n):
    for j in range(n):
        print("-", end='')
    print("X")
clear()

# *
for i in range(n):
    for j in range(i):
        print("-", end='')
    print("X", end="")
    for k in range(n-i):
        print("-", end='')
    print("X", end='')
    for l in range(n-i):
        print("-", end='')
    print("X", end="")
    print()
print("X"*(2*n)+"X")
for i in range(n):
    for l in range(n-i):
        print("-", end='')
    print("X", end="")
    for k in range(i):
        print("-", end='')
    print("X", end='')
    for j in range(i):
        print("-", end='')
    print("X", end="")

    print()
clear()

for i in range(n):
    for j in range(n-i):
        print("-", end="")
    for k in range(2*i+1):
        print(k+1, end='')
    print()
clear()

for i in range(n):
    for j in range(n-i):
        print("-", end="")
    if i % 2 == 0:
        for k in range(2*i+1):
            print(k+1, end='')
    else:
        for k in range(2*i+1, 0, -1):
            print(k, end='')
    print()
clear()
