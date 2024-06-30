cs101_students = ['Sanam','Sachin','Ajit','Deepa']

## List to tuple 
tup = tuple(cs101_students)
print ("List to Tuple: ",tup, type(tup))

## Tuple to List
lst = list(tup)
print ("Tuple to list: ",lst, type(lst))

##List to String
string = " ".join(cs101_students)
print ("List to String: ", string, type(string))

# ##String to List
str_lst = list(string.split( ))
print ("String to List: ",str_lst, type(str_lst))
