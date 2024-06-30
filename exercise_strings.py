s1=input("Enter first string:")
s2=input("Enter second string:")
print(s1+s2)

string_1="Welcome to Five days workshop"
s3=string_1.replace('e','o',3)
print("Replaced e with o:",string_1.replace('e','o',3))

print("total number of o's:",s3.count('o'))

s4=input("Enter a separator character")

print(s4.join("python"))