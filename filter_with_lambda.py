l = [i for i in range(1, 100)];
filtered_list=[];
for elem in l:
    if(elem%3 == 0):
        filtered_list.append(elem);
print(filtered_list)

l = [i for i in range(1, 100)];
filtered_list = list(filter(lambda x: (x%3 == 0), l))
print(filtered_list)
