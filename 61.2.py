lista = []
with open("ciagi.txt", "r") as plik:
    for i in plik.readlines():
        lista.append(i)
maks = 0
makslista = []
for i in range(0, len(lista), 2):
    ciong = [int(h) for h in lista[i+1].strip().split()]
    for i in ciong:
        for o in range(1, int(i ** (1 / 3)) + 2):
            if o ** 3 == i:
                makslista.append(i)
                maks = max(maks, i)

                break
print(maks, makslista)