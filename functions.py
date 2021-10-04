def print_hello(string, n):
    print(string * n)
    print()


print_hello('hello ', 5)


def circle_area(radius):
    return 3.142*radius*radius


print(circle_area(5))

# the return statement returns the value of the function of the caller


def avg(marks1, marks2):
    return (marks1 + marks2)/2


print(avg(50, 50))


def solve(a, b, c, d, e, f):
    x = (d*e-b*f)/(a*d-b*c)
    y = (a*f-c*e)/(a*d-b*c)
    return [x, y]


xsol, ysol = solve(2, 3, 4, 1, 2, 5)
print(xsol, ysol)

# function with default value

# default arguments


def print_fxn(string, n=1):
    print(string * n)
    print()


print_fxn('hello ', 5)
print_fxn('hello')

# calling two functions at a time


def f(x):
    return x**2


def g(x):
    return x**3


funcs = [f, g]
print(funcs[0](4), funcs[1](7), sep='\n')