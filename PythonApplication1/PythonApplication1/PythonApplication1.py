import itertools
import math

letters = "ABCDEFGH"

count = 0
for p in itertools.permutations(letters):
    perm = ''.join(p)
    if "AB" not in perm and "BC" not in perm and "BA" not in perm and "CB" not in perm:
        count = count + 1

print(count)
print(180 * math.factorial(5))
