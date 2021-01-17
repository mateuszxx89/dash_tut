from datetime import datetime

print(datetime.now())
print(datetime.now().hour)


def dekor(func):
    def wrap():
        if 9<= datetime.now().hour <=19:
            func()
        else:
            pass
    return wrap

@dekor
def pora_dnia():
    print('Wywołanie pora dnia')
    print('Godziny robocze')

pora_dnia()
