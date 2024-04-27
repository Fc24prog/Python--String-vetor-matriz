vet=[]
for i in range(0,30):
    vet.append(input('Numero:'))

x=input('Buscar numero:')
cont=0
for i in range(0,5):
    if vet[i]==x:
        cont=cont+1
print('Quantidade de vezes que o numero',x,'aparece:',cont)

#Ler um vetor de números inteiros de 30 posições.
#Depois, ler um número inteiro X, imprimir quantas vezes o número X
#aparece no vetor.
