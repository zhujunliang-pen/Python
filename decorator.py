# print_msg是外围函数,闭包
def print_msg():
    msg = "I'm closure"

    # printer是嵌套函数
    def printer():
        print(msg)

    return printer

# 这里获得的就是一个闭包
closure = print_msg()
# 输出 I'm closure
closure()

import functools
#decorator 函数装饰器
#arg  一个参数 ，不知有多少个参赛*args,  健值对参赛**kwargs{k1=v1, k2=v2}
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        print('args = {}'.format(*args))

        print('kwargs=', repr(kwargs))
        return func(*args, **kwargs)

    return wrapper

@log
def test(*p, **kwargs):
    print(test.__name__ + " param: {}".format(*p), repr(kwargs))
    
test("I'm a param", name='bill',age=43)
test("One Param")

print("------------带参数的装饰器---------------")
def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))

            return func(*args, **kwargs)

        return wrapper

    return decorator
    
@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__ + p)

test_with_param("aaa")

print("-------授权(Authorization)-----------")
"""def requires_auth(f):
    @functools.wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            authenticate()
        return f(*args, **kwargs)
    return decorated
"""
print("-------日志---------------")
def logit(func):
    @functools.wraps(func)
    def with_logging(*args, **kwargs):
        print(func.__name__ + " was called")
        return func(*args, **kwargs)
    return with_logging
 
@logit
def addition_func(x):
   """Do some math."""
   return x + x
 
result = addition_func(4)
# Output: addition_func was called



tup1 = (12, 34.56)
tup2 = ('abc', 'xyz')
# 以下修改元组元素操作是非法的。
# tup1[0] = 100 
# 创建一个新的元组
tup3 = tup1 + tup2
print (tup3)

t = ('te',)
t1 = 2,
t2 = t + t1
print(t2)


print("---------------")
def bar(param0, *param1, **param2):
    print (param0)
    print (param1)
    print (param2)
bar(0,1,2,a=2,b=3)