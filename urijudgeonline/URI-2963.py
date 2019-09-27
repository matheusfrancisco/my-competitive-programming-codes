n = int(input())
frist = 0
entro = 0
for i in range(n):
    voto = int(input())
    if i == 0:
        frist = voto
    else:
        if frist < voto:
            print("N")
            entrou = 1
            break

if entrou == 0:
    print("S")

