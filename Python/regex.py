####--------------REGULAR EXPRESSIONS----------------##

'''
Regex, or regular expressions, is like a search tool
for text. It helps find specific patterns or
characters in words, sentences, or data.

It’s widely used for:

Data Validation: Ensuring inputs like emails or phone
numbers are correctly formatted.

Text Search & Extraction: Pulling specific info
(e.g., URLs, emails) from text or data files.

Data Cleaning: Removing unwanted characters or
standardizing formats in data.

Web Scraping: Extracting details (prices, product names)
from websites.

Editing Text: Searching and replacing specific
words or patterns across files.

regex is a smart way to search and organize
text easily and efficiently.

'''
import re
#search return the first occurance as a match object
str1="fry cry dry try cry Dry Cry a "
##print(re.search("cry" , str1))

#findall  returns list of matches
##print(re.findall("cry",str1))

#[] accepts only one character
##print(re.findall("[aA-zZ]ry",str1))

# Use ^ to denote any character except
##whatever characters are between the brackets
str1="fry cry dry try cry Dry Cry a "
##print(re.findall("[^cC]ry",str1))
##print(re.findall("[^aA-gG]ry",str1))

#Replace/edit
#sub replaces one or many matches with a string
str1="fry cry dry try cry Dry Cry f "
print(re.sub("f","k", str1))
print(re.sub("ry","at", str1))


##compile method creates a regex pattern object
pat1=re.compile("cry")
##print(re.search(pat1,str1))



##The backslash (\) in regex is used to define
##special characters or escape characters that
##have a special meaning in regex.

str2="ABC Tr 23 Y6 8u #@&*()+-_"

##\d	any digits (numbers from 0-9)
print(re.search("\d",str2))
print(re.findall("\d",str2))

##[^\d]=\D
##\D	any string which DOES NOT contain digits
print(re.findall("\D",str2))

##\s	any string which contains a white space
##        character
print(re.search("\s",str2))
print(re.findall("\s",str2))

##[^\s]=\S
##\S	any string which DOES NOT contain a white
##        space character
print(re.findall("\S",str2))

##\w	any string contains  word characters
##        (characters from a to Z, digits from 0-9,
##        and the underscore _ character)
##w=[a-z 0-9 _]
print(re.findall("\w",str2))

##\W	any string which DOES NOT contain any word characters

print(re.findall("\W",str2))









