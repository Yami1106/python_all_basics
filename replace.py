#returns a copy of the string in which the occurances of old have been replaced with new
string_1 = "Hello Python, the string handling features are the best"
print ("Actual string: ", string_1)

#string.replace returns a copy of the string and doesn't alter the orignal string.
print ("Replaced occurrance of 'th': ", string_1.replace('th','!!',1))   # replace only first occurrance
print ("Replaced occurrance of 'th': ", string_1.replace('th','!!',3))   # replace all occurrances
print (string_1)
