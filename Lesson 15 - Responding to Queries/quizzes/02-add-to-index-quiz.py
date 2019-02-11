# Define a procedure, add_to_index,
# that takes 3 inputs:

# - an index: [[<keyword>,[<url>,...]],...]
# - a keyword: String
# - a url: String

# If the keyword is already
# in the index, add the url
# to the list of urls associated
# with that keyword.

# If the keyword is not in the index,
# add an entry to the index: [keyword,[url]]

index = []


def add_to_index(index, keyword, url):
    # Loop through index for each entry
    for entry in index:
        # The first index should match the keyword, append url to the second index (the list)
        if entry[0] == keyword:
            entry[1].append(url)
            # Use return since we want to end the procedure
            return
    # Append new list of list to the index if keyword does not already exist
    index.append([keyword, [url]])


# add_to_index(index,'udacity','http://udacity.com')
# add_to_index(index,'computing','http://acm.org')
# add_to_index(index,'udacity','http://npr.org')
# print index
# >>> [['udacity', ['http://udacity.com', 'http://npr.org']],
# >>> ['computing', ['http://acm.org']]]
