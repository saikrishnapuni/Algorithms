# Given n, radius of a circle with (0,0) as center, write a linear time algorithm to
# compute the number of lattice (integer) points inside the circle.
import math

def solve(r):
    points = 0

    for i in range(r - 1, -1, -1):
        linePoints = int(math.sqrt(r*r - i*i - 1))
        points += linePoints

    return 4 * points + 1


print(solve(2))  # 5
print(solve(3))  # 25
            