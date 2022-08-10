from functools import reduce
x=[1,2,3,4]
def cube(a):
    return a*a*a
y=map(cube,x)
print(y)
print(list(y))
z=map(lambda a:a+5,x)
print(z)
print(list(z))
def gt5(n):
    return n > 5
p=filter(gt5,x)
print(list(p))
q=filter(lambda a:a>3,x)
print(q)
print(list(q))
r=reduce(lambda a,b:a+b,x)
print(r)








