roll = (1,2,3,4,5)
name = ('Sanam', 'Sachin', 'Ajit', 'Deepa','Piyush')
marks = [10,5.5,8,9,8.5]
subject = ['Electronics','C-Prog', 'Data-structure','Digital Circuits']

information = [0]

information.insert(5,name)
information.insert(2,name)
information.insert(0,marks)
information.insert(4,subject)

print (information)
print (information[0])
print (information[2][2])
print (information[4][3])

