import re

# RegEx module methods
# Use RegEx to check if a string contains the specified search pattern
Info = 'SicKickForm of human kind is a nickname for a 18 years old boy'
print("search")
print(re.search('SicKickForm', Info))
print(re.search('SicKickForm', Info).span())
print(re.search('SicKickForm', Info).string)
print(re.search('SicKickForm', Info).group())
# Start of string
print(bool(re.search('\ASicK', Info)))
# Start or end of a word
print(bool(re.search(r'\bSicK', Info)))
print(bool(re.search(r'Form\b', Info)))
# Middle of a word
print(bool(re.search(r'\BKick', Info)))
# End of a word
print(bool(re.search('boy\Z', Info)))
# Starting with
print(bool(re.search('^S', Info)))
# Ending with
print(bool(re.search('y$', Info)))
print("findall")
print(re.findall('f', Info))
# Lower case charcaters in the domain
print(re.findall('[a-h]', Info))
print(re.findall('[abc]', Info))
print(re.findall('[12345]', Info))
# Single digits in the domain
print(re.findall('[6-9]', Info))
# Double digits in the domain
print(re.findall('[1-5][5-8]', Info))
# Lower and upper case charcaters in the domain
print(re.findall('[a-hA-L]', Info))
# Except given characters
print(re.findall('[^abc]', Info))
# Any character in the blank spot
print(re.findall('o.', Info))
# Zero or more characters in the blank sport
print(re.findall('i.*F', Info))
# One or more characters in the blank sport
print(re.findall('i.+F', Info))
# Zero or one characters in the blank sport
print(re.findall('i.?F', Info))
# Specified amount of  characters in the blank sport
print(re.findall('i.{2}F', Info))
# Either or
print(re.findall('boy|girl', Info))
# Digits of String
print(re.findall('\d', Info))
# String without digits
print((re.findall('\D', Info)))
# Spaces of string
print(re.findall('\s', Info))
# String without spaces
print(re.findall('\S', Info))
# Letters digits underscores of string
print(re.findall('\w', Info))
# String without letters digits underscores
print(re.findall('\W', Info))
print("split")
print(re.split('i', Info, 3))
print("sub")
print(re.sub('i', '/', Info, 3))
