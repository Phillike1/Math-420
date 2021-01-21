# Problem 1
L=[1,2,3,4,5,6,7,8,9,10]

# Python program to get average of a list 
def Average(L): 
    return sum(L) / len(L)

print(min(L),max(L),Average(L))

# Problem 2

x = int(10.25)
print(x)
year = x
print(year)
year += 2
print(year)
print(x)

# int is immutable

y = 'The Doors'
print(type(y))
String_1 = y
print(String_1)
String_1 += ': Stange Days'
print(String_1)
print(y)

# str is immutable

z = list(('2','3','5','7','11'))
print(z)
List_1 = z
print(List_1)
List_1 += ('4','6','10','14','22')
print(List_1)
print(z)
print(type(z))

# list is mutable

q = ("The Soft Parade", 1969)
print(q)
my_tuple = q
print(my_tuple)
my_tuple += (1,"Tuple")
print(my_tuple)
print(q)
print(type(q))

# tuple is immutable

GEEK = {'g', 'e', 'k'}
t = GEEK
print(t)
t.add('s') 
print(t)
print(GEEK)
print(type(t))

# set is mutable

# Problem 3

from calculator import add 
from calculator import mult
from calculator import sqrt
def hyp(a,b):
    return sqrt(add(mult(a,a),mult(b,b)))
print(hyp(3,4))

# Problem 4

A = ['a', 'b', 'c']
from itertools import chain, combinations
def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

print(list(powerset(A)))
