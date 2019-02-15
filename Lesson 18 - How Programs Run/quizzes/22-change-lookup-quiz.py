# Change the lookup procedure
# to now work with dictionaries.

# def lookup(index, keyword):
#     for entry in index:
#         if entry[0] == keyword:
#             return entry[1]
#     return None


def lookup(index, keyword):
    if keyword in index:
        return index[keyword]
    return None

students = {
  'Steven': 25,
  'Steph': 100
}

print(lookup(students, 'Steven'))
