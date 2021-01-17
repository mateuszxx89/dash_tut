def dekorator(func):
    print('python')
    return func

@dekorator
def hello_world():
    print('hello world')

hello_world()