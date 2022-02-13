n = input("Inserir n° hexadecimal: ")

# Valores númericos de A a F

a=10
b=11
c=12
d = 13
e = 14
f = 15

## Separando cada caractere

l = []

t = len(n) ## Tamanho da string
count = -1
while count < (t-1):
    count = count + 1
    l.append(n[count])

## Verificando e convertendo caracteres 

listaHex = [] ## Recebe tanto números de 0 a 9 como letras convertidas de A a F para seu respectivo valor

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

## Operando cada número

tHex = len(listaHex)
base = tHex - 1 ## tHex - 1
zero = -1
index = 0
while index < tHex:
    listaHex[index] = listaHex[index]*16**base
    if base is not zero:
        base = base - 1
    index = index + 1

## Soma dos números
    
soma = sum(listaHex)

print("Decimal: {}".format(soma))
