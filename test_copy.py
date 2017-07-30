import copy
# print(copy.__file__)

a = [1, 2, 3]
b = [4, 5, 6]
# c = [a, b]
c = [[1], [2], [3]]

# using normal assignment operations to copy:
d = c
# True - d is the same object as c
print("normal assign:id(c)==id(d):{},id(c)=={},id(d)={}".format(id(c)==id(d), id(c), id(d)))
# True - d[0] is the same object as c[0]
print("normal assign:id(c[0])==id(d[0]):{},id(c[0])=={},id(d[0])={}".format(id(c[0])==id(d[0]), id(c[0]), id(d[0])))
print()

# using a shallow copy
d = copy.copy(c)
# False - d is now a new object
print("shallow copy:id(c)==id(d):{},id(c)={},id(d)={}".format(id(c) == id(d),id(c),id(d)))
# True - d[0] is the same object as c[0]
print("shallow copy:id(c[0]) == id(d[0]):{},id(c[0])={},id(d[0])={}".format(id(c[0])==id(d[0]), id(c[0]), id(d[0])))
print()

# using a deep copy
d = copy.deepcopy(c)
# False - d is now a new object
print("deep copy:id(c)==id(d):{},id(c)={},id(d)={}".format(id(c)==id(d),id(c),id(d)))
# False - d[0] is a new object
print("deep copy:id(c[0]) == id(d[0]):{},id(c[0])={},id(d[0])={}".format(id(c[0])==id(d[0]), id(c[0]), id(d[0])))