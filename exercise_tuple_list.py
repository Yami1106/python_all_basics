l1=[23,1,4,56,123,5,76]
l2=[]
for i in l1:
    l2.append(str(i))

print(l2)

tup_1 = (1, 2, 3, 4, 1, 2, 1, 5, 3, 1, 2, 6)

l3 = []
l4 = []

for item in tup_1:
    if item in l3:
        if item not in l4:
            l4.append(item)
    else:
        l3.append(item)

print("Repeated items are:", ', '.join(map(str,l4)))



