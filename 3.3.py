from timeit import default_timer as timer

def bubblesort(a):
    list = a
    n = len(list)

    start = timer()
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    end = timer()
    print(list)
    print("Tempo final", end - start)


def newbubblesort(a):
    list = a
    n = len(list)

    start = timer()
    for i in range(n):
        for j in range(0, n-i-1):
            if list[j] > list[j+1]:
                list[j], list[j+1] = list[j+1], list[j]
    end = timer()
    print(list)
    print("Tempo final", end - start)


lista = [54, 26, 93, 17, 77, 31, 44, 55, 20]
print(lista)
bubblesort(lista)
newbubblesort(lista)
