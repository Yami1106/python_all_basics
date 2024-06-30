fact=1;
for i in range(1,7):
    fact=fact*i;
    print(fact)
print(fact)

import functools as f

fact=f.reduce(lambda x,y: x*y,[i for i in range(1,7)],1)

print(fact)