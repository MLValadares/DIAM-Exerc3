from timeit import default_timer as timer


def a(str1, str2):
    a = [*str1]
    b = [*str2]
    xa = range(len(str1))
    xb = range(len(str2))
    start = timer()
    passos = 0
    for n1 in xa:
        for n2 in xb:
            passos += 1
            if a[n1] == b[n2]:
                b[n2] = None
                break
    end = timer()
    print("Tempo final", end-start)
    print("Número de passos", passos)
    # Atenção: pode dar True quando o str1 tem mais caracteres que o str2
    for x in b:
        if x is not None:
            return False
    return True


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
    a = [*str1]
    start = timer()
    b = permutation(a)
    passos = len(str1)
    lista = []
    # Para estes ciclos for não consediramos como passos, porque consiste apenas na agregação caracteres individuas dentro de lista para uma string
    for x in b:
        k = ""
        for i in x:
            k += i
        lista.append(k)
    for x in lista:
        passos +=1
        if x == str2:
            end = timer()
            print("Tempo final", end - start)
            print("Número de passos", passos)
            return True
    end = timer()
    print("Tempo final", end - start)
    print("Número de passos", passos)
    return False
    # print(permutation(a))

# def permutatio(str):
#     k = permutation(str, 0)
#     print("Número de passos", k[1])
#     return k[0]


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
    # print(res1),print(res2)

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
print("Exerc A")
print(a(str1,str2))
print()
print("Exerc B")
print(b(str1,str2))
print()
print("Exerc C")
print(c(str1,str2))
print()
print("Exerc D")
print(d(str1,str2))
print()

# Em termos de passos de execução é difícil dizer, visto que no exerc B usamos um função de sorting próprio do python
# Em termos de tempo, a solução B parece ser a solução mais rápida.

# A solução C é a pior porque obriga ao computador a criar tudas as possibilidades, que costa mais quer em tempo, quer em passos de execução