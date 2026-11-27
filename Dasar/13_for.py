import os
os.system("cls")
tinggi = 5

n = int(input("input nomor: "))

# pertama
for a in range(1, n + 1):
    for j in range(n, a, -1):
        print(" ", end="")

    for x in range(1, a + 1):
        print("*", end="")

    print()


# kedua
for a in range(1, n + 1):
    for j in range(1, a):
        print(" ", end="")

    for x in range(n, a - 1, -1):
        print("*", end="")

    print()


# ketiga
for a in range(1, n + 1):
    for j in range(1, a + 1):
        print("*", end="")

    print()


# keempat
for a in range(1, n + 1):
    for j in range(n, a - 1, -1):
        print("*", end="")

    print()


# kelima
for a in range(1, n + 1):
    for j in range(n, a, -1):
        print(" ", end="")

    for x in range(1, 2 * a):
        print("*", end="")

    print()

