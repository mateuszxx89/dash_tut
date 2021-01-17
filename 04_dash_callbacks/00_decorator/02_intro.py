
def dekorator(func):
    def wrapper():
        func()
        print('wywolanie funkcji wrapper')
    return wrapper

@dekorator
def func_2():
    print('wywołanie func 2')

func_2()