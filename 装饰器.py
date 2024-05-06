from functools import wraps
from functools import reduce


def test(flag):
    def decorate(func):
        @wraps(func)
        def wapper(*args):
            if flag:
                ae = sum(*args)
                print(ae)
                return func(*args)
            else:
                print('无权限')

        return wapper

    return decorate


@test(flag=True)
def add(*args):
    a = reduce(lambda x, y: x + y, *args)
    print(a)


b = [i for i in range(10)]
add(b)
