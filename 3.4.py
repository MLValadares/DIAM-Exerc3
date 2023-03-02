from timeit import default_timer as timer


def a(str1, str2):
    a=[*str1]
    b=[*str2]
    x = range(len(str1))
    start = timer()
    passos = 0
    for n1 in x:
        for n2 in x:
            passos += 1
            if a[n1] == b[n2]:
                b[n2] = None
                break;
            # print(b)
    end = timer()
    print("Tempo final", end-start)
    print("Número de passos", passos)
    # print(b)
    for x in b:
        if x is not None:
            return False;
    return True;


def b(str1, str2):
    passos = 3
    start = timer()
    a = sorted([*str1])
    b = sorted([*str2])
    if a == b:
        end = timer()
        print("Tempo final", end - start)
        print("Número de passos", passos)
        return True
    end = timer()
    print("Tempo final", end - start)
    print("Número de passos", passos)
    return False


def c(str1, str2,):
    a = sorted([*str1])
    lista = []

    return False


def d(str1, str2):
    return False


str1 = "amor"
str2 = "roma"
print(b(str1,str2))
# print(b(str1,str2))