# Define a procedure, biggest, that takes three
# numbers as inputs and returns the largest of
# those three numbers.


def bigger(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2


def biggest(n1, n2, n3):
    return bigger(bigger(n1, n2), n3)


# print biggest(3, 6, 9)
# >>> 9

# print biggest(6, 9, 3)
# >>> 9

# print biggest(9, 3, 6)
# >>> 9

# print biggest(3, 3, 9)
# >>> 9

# print biggest(9, 3, 9)
# >>> 9
