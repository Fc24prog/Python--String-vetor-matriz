vet=[]
cont=0
for i in range(0,4):
    vet.append(input('Numero: '))

for i in range(0,4):
    if vet[i]%2==0:
        cont=cont+1
print('Quantidade de numeros pares no vetor:',cont)
