# Opening up the broken json file an reading data from it:
file = open('/Users/lujan/PycharmProjects/combining_files/rawDataBetterCodeHub.json', 'r')
data = file.readlines()
file.close()

# Adding the block separator brackets in the beginning and
# the end of the file:
data.insert(0, '[\n')
data.append(']\n')

# Appending comas whenever one of the mini json files terminates:
for i, line in enumerate(data):
    if line == '}\n':
        data[i] = '},\n'

# Removing the coma from the last mini json file:
data[-2] = '}\n'

# Writing the redacted data to a proper json file:
with open('jqc_redacted.json', 'w') as file:
    for line in data:
        file.write(line)
