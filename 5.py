vet=[]
for i in range(0,16):
    a=input('Numero: ')
    vet.append(a)
print('Vetor original:',vet)
for i in range(0,8):
    aux=vet[i]
    vet[i]=vet[i+8]
    vet[i+8]=aux
print('Vetor trocado:',vet)







#Leia um vetor de 16 posições e troque as 8 primeiras posições pelas 8 últimas
#posições. Imprima o vetor original e o vetor trocado.
