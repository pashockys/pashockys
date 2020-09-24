from functools import wraps
def simple_function():
    print('1')
def simple_function2():
    print('2')
    return 'vova'
def to_lower_case(txt):
    return txt.lower()
def to_upper_case(txt):
    return txt.upper()
list_of_strings = ['sfsdf', 'sdfds', 'Vova']
list_of_functions = [simple_function2, simple_function]
list_of_str_func = [to_lower_case, to_upper_case]
print(f'zalupa {list_of_functions[0]()}')
list_of_functions[0]()

# testing map func
for z in list_of_str_func:
    for i in map(z, list_of_strings):
        print(i)

# testing that function can return function
def function_returning_function():
    return simple_function2()
print(f'test_return_func {function_returning_function()}')

# testing simple func in func
def vova1(txt):
    a = txt
    print('at first we were here')
    def vova2():
        return print(f'vova2 say {a}')
    print('then we were here')
    return vova2

vova1('zalupa')()

# multiply
def multiply(out_num):
    def internal(int_num):
        return out_num*int_num
    return internal

mult_by_9 = multiply(9)

print(f'opachki {mult_by_9(5)}')
# contdown function
def countdown(num):
    def inner_func():
        nonlocal num
        print(num)
        num -= 1
    return inner_func

death_10 = countdown(10)
death_10()
death_10()

death_10.scream = 'aaaaaaa'

print(death_10.scream)
# func in func with atributes
def outter(a, b):
    def inner():
        def add():
            return a+b
        def mult():
            return a*b
        def sub():
            return a-b
        inner.add = add
        inner.mult = mult
        inner.sub = sub
    return inner

func1 = outter(4,4)
func1()
print(func1.add())
print(func1.sub())
print(func1.mult())

# actually decorating
# multiply with decorating
def actual_decorator(func):
    print("This is decorator")
    return func
@actual_decorator
def decorated_func(a, b):
    print("This func is decorated")
    return a+b
print(decorated_func('a', 'b'))

# decorator with inner function

print(40*'===')
def actual_decorator(func):
    print("This is decorator")
    def inner(*args, **kwargs):
        print(f"This is inner func in decorator called '{func.__name__}'\n"
              f"it has {args} {kwargs} as arguments")
        return func(*args, **kwargs)
    return inner
@actual_decorator
def decorated_func(a, b):
    print("This func is decorated")
    return a+b
print(decorated_func('a', 'b'))

# decorator that check if all arguments are string

print(40*'===')
def decorator_that_check_type(func):
    print('we are inside decorator')
    @wraps(func)
    def inner_func(*args):
        print('inside inner func in decorator')
        result = [i for i in args if type(i) is str]
        return func(*result)
    return inner_func

@decorator_that_check_type
def func_with_variables(*args):
    print(f'{args}')
list1 = [4, 5]
func_with_variables(4, '3', 'dddd', list1)

print(f'this is func name\n{func_with_variables.__name__}')