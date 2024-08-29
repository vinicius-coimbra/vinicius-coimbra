
lista = []
for i in range(6):
    n1 = int(input('\033[1;32m:\033[m'))
    lista.append(n1)
contado = 0
for i in lista:
        if i % 2 == 0:
            print(i)
            contado  += i
              
print(contado) 