n = "A37E"

# Letras
a=10
b=11
c=12
d = 13
e = 14
f = 15


l = []
print("Antes:", l)

t = len(n) ## Tamanho da string
count = -1
while count < (t-1):
    count = count + 1
    l.append(n[count])

print("Depois:", l)

## Verificando o caractere 

listaHex = []

for k in range(0,len(l)):
    if l[k] == "0":
        listaHex.append(int(l[k]))
    if l[k] == "1":
        listaHex.append(int(l[k]))
    if l[k] == "2":
        listaHex.append(int(l[k]))
    if l[k] == "3":
        listaHex.append(int(l[k]))
    if l[k] == "4":
        listaHex.append(int(l[k]))
    if l[k] == "5":
        listaHex.append(int(l[k]))
    if l[k] == "6":
        listaHex.append(int(l[k]))
    if l[k] == "7":
        listaHex.append(int(l[k]))
    if l[k] == "8":
        listaHex.append(int(l[k]))
    if l[k] == "9":
        listaHex.append(int(l[k]))
    if l[k] == "A":
        listaHex.append(a)
    if l[k] == "B":
        listaHex.append(b)
    if l[k] == "C":
        listaHex.append(c)
    if l[k] == "D":
        listaHex.append(d)
    if l[k] == "E":
        listaHex.append(e)
    if l[k] == "F":
        listaHex.append(f)

print("Lista de números hex.:", listaHex)

tHex = len(listaHex)
base = tHex - 1 ## tHex - 1
zero = -1
index = 0
while index < tHex:
    listaHex[index] = listaHex[index]*16**base
    if base is not zero:
        base = base - 1
    index = index + 1
        


'''
tHex = len(listaHex) 
base = (tHex - 1)

index = 0

while index < tHex:
    listaHex[index] = listaHex[index]*16**base

    index = index + 1
    while base >= 0:
        base = base - 1
'''
print("atual", listaHex)
print(sum(listaHex))
