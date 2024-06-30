a = 10;
def func():
    a = 15; # local to func()
func()
print(a) # prints the global a value

a = 10;
def func():
    global a;
    a = 15; # refers to global a
func()
print(a) # prints the global a value
