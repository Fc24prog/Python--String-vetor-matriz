def busca(letra,v1):
    for i in range(0,len(v1)):
        if letra == v1[i]:
            return i
    return -1

def pegaLetra(frase,v1,v2):
    for i in range(0,len(frase)):
        if frase[i] != " ": #tirando os espacos vazios
            posicao = busca(frase[i],v1)
        if posicao != -1:
            v2[posicao] += 1
        else:
            v1.append(frase[i])
            v2.append(1)

frase = input("frase: ")
vetLetra=[]
vetQtd = []
pegaLetra(frase,vetLetra,vetQtd)
print (vetLetra)
print (vetQtd)

#Fazer um programa para ler uma frase e guardar as
#letras em um vetor e a quantidade de vezes que
#aparece em um outro vetor
