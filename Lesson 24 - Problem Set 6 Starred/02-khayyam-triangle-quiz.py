# Double Gold Star

# Khayyam Triangle

# The French mathematician, Blaise Pascal, who built a mechanical computer in
# the 17th century, studied a pattern of numbers now commonly known in parts of
# the world as Pascal's Triangle (it was also previously studied by many Indian,
# Chinese, and Persian mathematicians, and is known by different names in other
# parts of the world).

# The pattern is shown below:

#                    1
#                   1 1
#                  1 2 1
#                 1 3 3 1
#                1 4 6 4 1
#                   ...

# Each number is the sum of the number above it to the left and the number above
# it to the right (any missing numbers are counted as 0).

# Define a procedure, triangle(n), that takes a number n as its input, and
# returns a list of the first n rows in the triangle. Each element of the
# returned list should be a list of the numbers at the corresponding row in the
# triangle.


# Default array list
l = [[1], [1, 1]]

# Build khayyam triangle
def build_khayyam():
    i = 0
    s = 0
    # Loop through first 30 terms
    for x in range(1, 30):
        s = 0
        i = 0
        temp = [1]
        # Loop through length
        for y in l[len(l) - 1]:
            s += y
            i += 1
            if i == 2:
                temp.append(s)
                s = y
                i = 1
        # Perform append sequence
        temp.append(1)
        l.append(temp)


# Call khayyam function
build_khayyam()


def triangle(n):
    res = []
    for i in range(0, n):
        res.append(l[i])
    return res


# For example:

# print triangle(0)
# >>> []

# print triangle(1)
# >>> [[1]]

# print triangle(2)
# >> [[1], [1, 1]]

# print triangle(3)
# >>> [[1], [1, 1], [1, 2, 1]]

# print triangle(6)
# >>> [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1], [1, 4, 6, 4, 1], [1, 5, 10, 10, 5, 1]]
