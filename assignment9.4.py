import re

s = '  Hello  World   From Pankaj \t\n\r\tHi There  '

print('Remove all spaces using RegEx:\n', re.sub(r"\s+", "", s), sep='')
print('Remove leading spaces using RegEx:\n', re.sub(r"^\s+", "", s), sep='')
print('Remove trailing spaces using RegEx:\n', re.sub(r"\s+$", "", s), sep='')
print('Remove leading and trailing spaces using RegEx:\n', re.sub(r"^\s+|\s+$", "", s), sep='')