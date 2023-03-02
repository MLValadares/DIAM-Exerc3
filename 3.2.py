# poema = " Eu hoje fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo / Por isso eu fiz um samba bem pra frente / Dizendo realmente o que é que eu acho / Eu acho que o meu samba é uma corrente / E coerentemente assino embaixo / Hoje é preciso refletir um pouco / E ver que o samba está tomando jeito / Só mesmo embriagado ou muito louco / Pra contestar e pra botar defeito / Precisa ser muito sincero e claro / Pra confessar que andei sambando errado / Talvez precise até tomar na cara / Pra ver que o samba está bem melhorado / Tem mais é que ser bem cara de tacho / Não ver a multidão sambar contente / Isso me deixa triste e cabisbaixo"
poema = "ola oa"
vogais = ["A", "E", "I", "O", "U"]
lista = [0, 0, 0, 0, 0]
for x in poema:
    if x == "a" or x == "A":
        lista[0] = lista[0] + 1
    if x == "e" or x == "E":
        lista[1] = lista[1] + 1
    if x == "i" or x == "I":
        lista[2] = lista[2] + 1
    if x == "o" or x == "O":
        lista[3] = lista[3] + 1
    if x == "u" or x == "U":
        lista[4] = lista[4] + 1

total = 0
for x in lista:
    total = total + x
print("Número total de vogais: ", total)

print("A", lista[0])
print("E", lista[1])
print("I", lista[2])
print("O", lista[3])
print("U", lista[4])

# max_value = max(lista)
# max_index = lista.index
# print(max_index)

indices = [index for index, item in enumerate(lista) if item == max(lista)]
if len(indices) > 1:
    print("Há vários vencedores")
for x in indices:
    print(vogais[x])
