from timeit import default_timer as timer


def a(str1, str2):
    a = [*str1]
    b = [*str2]
    for x in a:
        for y in b:
            if x == y:
                print(b[y])
                break;
    print(a)
    print(b)


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


str1 = "am or"
str2 = "ro ma"
print(a(str1,str2))