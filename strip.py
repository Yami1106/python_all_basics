# strip unwanted characters from beginning and end of string
string_1 = "0 00Hello Python, the string handling features are awesome00"
print ("Actual string: ", string_1)
print (len(string_1))
print (string_1.strip())
print (len(string_1.strip()))
print (string_1.strip("0"))
print (len(string_1.strip("0")))
print (string_1.strip("0 "))
#Note the addition of a space after '0' in the last strip statement. Also, the orignal string is not at all altered during this command.
