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
    l = []
    a = [*str1]
    b= permutation(a)
    for x in b:
        k =""
        for i in x:
            k += i
            # print(k)
        print(k)


    print(permutation(a))

def permutation(str):
    if len(str) == 0:
        return []
    if len(str) == 1:
        return [str]
    l = []
    for i in range(len(str)):
        n = str[i]

        remStr = str[:i] + str[i+1:]
        for x in permutation(remStr):
            l.append([n] + x)
    return l

def d(str1, str2):
    start = timer()
    passos=0
    letras_1=[]
    letras_2=[]

    for c in str1:
        passos+=2
        count=count_letters(str1,c)
        letras_1.append((c,count))

    for c in str2:
        passos+=2
        count=count_letters(str2,c)
        letras_2.append((c,count))

    letras_1.sort()
    letras_2.sort()
    res1=[*set(letras_1)]
    res2=[*set(letras_2)]
    print(res1),print(res2)

    if res1==res2:
        passos+=5
        end=timer()
        print("Tempo final", end - start)
        print("Número de passos", passos)
        return True

    passos+=4
    end=timer()
    print("Tempo final", end - start)
    print("Número de passos", passos)
    return False

def count_letters(word, char):
    count = 0
    for c in word:
        if char == c:
            count += 1
    return count

str1 = "amor"
str2 = "roma"
print(b(str1,str2))
# print(b(str1,str2))