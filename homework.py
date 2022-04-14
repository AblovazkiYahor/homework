
# Homework on Thursday (31.03.2022)
print('Exercise 1:')
print()
def id_cell_1():
    a = 100
    b = 100
    c = 100
    print(id(a))
    print(id(b))
    print(id(c))
    print(a is b is c)
id_cell_1()
print('-----------------------------------------------------------------!')


print('Exercise 2:')
print()
e = 300
f = str(e)
print(id(e))
print(id(f))
print('-----------------------------------------------------------------')

print('Exercise 3: ')
def id_cell_3():
    a = 10
    b = str(100)
    c = bool(100)
    e = str(300)
    f = e
    print(id(a))
    print(id(b))
    print(id(c))
    print(id(e))
    print(id(f))
id_cell_3()



