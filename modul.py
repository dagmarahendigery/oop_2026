def dodaj(a, b):
    return a + b


def dodaj2(*args):
    print(args)
    print(type(args))


args = (1, 2, 3, 4)

wynik = dodaj2(*args)

print(args)
print(type(args))




