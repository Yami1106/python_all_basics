l = [1, 2, 3, 4, 5];
for i in range(len(l)):
    l[i] = l[i]**2;
print(l)

sqr = list(map(lambda x: x**2, [1, 2, 3, 4, 5])) # Returns 
print(sqr)

incr = list(map(lambda x: x+1, [1,3,5,7,6]))
print(incr)

import math
sqrt_list = list(map(math.sqrt, [1, 4, 9, 25]))
print(sqrt_list)