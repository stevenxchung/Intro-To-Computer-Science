inner_pattern = '...'
cellStore = {'...': 1, '..x': 2, '.x.': 4, '.xx': 8,
             'x..': 16, 'x.x': 32, 'xx.': 64, 'xxx': 128}
val = cellStore[inner_pattern]
print(val)