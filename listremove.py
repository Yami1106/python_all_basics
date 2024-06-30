#syntax: listname.remove(element)

cs101_students = ['Sanam','Sachin','Ajit','Deepa','Ajit']
print ("Element removed is: ",cs101_students.remove('Ajit'))      # remove method returns nothing
print ("Updated list is: ",cs101_students)                        # It will remove the first matching element
#cs101_students.remove('Saurav')       # Element 'Saurav' is not present - hence this will give value error
