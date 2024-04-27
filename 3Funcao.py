def vetSemRep(vet):
    vetAux = []
    for i in range(0,len(vet)):
        achou = False
        for j in range(0,len(vetAux)):
            if vet[i] == vetAux[j]:
                achou = True
                if not achou:
                    vetAux.append(vet[i])
    return vetAux

vet=[]
vetNovo=[]
for i in range(0,5):
    vet.append(int(input("elem:")))

vetNovo = vetSemRep(vet)
print ("vet:", vet)
print ("vet novo:", vetNovo)

#Fazer um módulo para receber um vetor como
#parâmetro e retornar um outro vetor sem repetições
