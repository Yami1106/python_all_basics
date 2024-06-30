n=int(input("Enter a number to find its factorial: "))
factorial=1
for i in range(1,n+1):
    factorial=factorial*i

print(factorial)

n2=int(input("Enter a 3 digit number: "))
sum=0
while n2>0:
    sum=sum+(n2%10)
    n2=int(n2/10)
    
print("Sum of digits is: ",sum)