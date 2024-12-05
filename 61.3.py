lista = []
with open("bledne.txt", "r") as plik:
    for i in plik.readlines():
        lista.append(i)
blednelista = []
for i in range(0, len(lista), 2):
    n = int(lista[i].strip())
    ciong = [int(h) for h in lista[i+1].strip().split()]
    roznica = ciong[1] - ciong[0]
    z = -1
    for j in range(2, n):
        if roznica != ciong[j] - ciong[j-1]:
            if z == -1:
                if j + 1 < n and ciong[j+1] - ciong[j-1] == (2 * roznica):
                    z = j
                elif j > 0:
                    z = j - 1
            break
    if z != -1:
        blednelista.append(ciong[z])
print(blednelista)