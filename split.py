string_1 = "Hello Python, the string handling features are awesome"
print ("Actual string: ", string_1)

string_to_list = (string_1.split())
print (string_to_list)
print (len(string_to_list))

string_to_list = string_1.split(" ",0) #The list contains only the zeroth element
print (string_to_list)
print (len(string_to_list))
print (string_1)