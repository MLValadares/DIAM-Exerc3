from timeit import default_timer as timer


def a(str1, str2):
    a=[*str1]
    b=[*str2]
    x = range(len(str1))
    for n1 in x:
        for n2 in x:
            if a[n1] == b[n2]:
                b[n2] = None
    for x in b:
        if x is not None:
            return False;
    return True;


def b(str1, str2):
    a = sorted([*str1])
    b = sorted([*str2])
    if a == b:
        return True
    return False


def c(str1, str2,):
    a = sorted([*str1])
    lista = []

    return False


def d(str1, str2):
    return False


str1 = "amor"
str2 = "roma"
print(a(str1,str2))
print(b(str1,str2))