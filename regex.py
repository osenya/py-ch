# searching for a word in a string
import re

if re.search('heighten', ' The political tension was heightened by his remarks'):
    print(' The word is present in the statement')
else:
    print('Missing word')

allHigh = re.findall('high', 'The tension was very high when his anger was heightened by the high cases of robbery ')
for i in allHigh:
    print(i)

