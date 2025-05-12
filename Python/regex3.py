import re
#\b used as a word boundary to define the start and end of a word


str1="try app tapp capp"
print(re.search(r"\bapp\b", str1))

#Quantifiers
#matching zero , one or many
#zero or one (?)
s1="app apps appsss appsss Apppss"
print(re.findall(r"apps?",s1))

#one or many (+)
print(re.findall(r"apps+",s1))

#zero or many (*) all
print(re.findall(r"apps*",s1))









# for matching large block and capturing a part of it




