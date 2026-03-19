n = int(input())

for x in range(n):
    print(" " * (n - x - 1) + "*" * (2 * x + 1))

for x in range(n - 1):
    print(" " * (x + 1) + "*" * (2 * n - 2 * x - 3))
