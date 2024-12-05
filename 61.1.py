lista = []
with open("ciagi.txt", "r") as plik:
    for i in plik.readlines():
        lista.append(i)
x = 0
y = 0
for i in range(0, len(lista), 2):
    n = int(lista[i].strip())
    ciong = [int(h) for h in lista[i+1].strip().split()]
    z = 1
    roznica = ciong[1] - ciong[0]
    for o in range(2, n):
        if ciong[o] - ciong[o - 1] != roznica:
            z = 0
            break
    if z == 1:
        x += 1
        y = max(y, roznica)
print("ilosc ciagow:", x, "najwieksza roznica:", y)
