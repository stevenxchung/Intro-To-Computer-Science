# Define a procedure, lookup,
# that takes two inputs:

# - an index
# - keyword

# The procedure should return a list
# of the urls associated
# with the keyword. If the keyword
# is not in the index, the procedure
# should return an empty list.

index = [['udacity', ['http://udacity.com', 'http://npr.org']],
         ['computing', ['http://acm.org']]]


def lookup(index, keyword):
    # Same as before, loop through index for each entry and find the entry that matches the key
    for entry in index:
        if entry[0] == keyword:
            # Returns array of url(s) if keyword is found
            return entry[1]
    # Return empty array if not found
    return []


# print lookup(index,'udacity')
# >>> ['http://udacity.com','http://npr.org']
