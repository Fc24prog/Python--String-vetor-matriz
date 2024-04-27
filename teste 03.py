mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(int(input("Entre com o elemento: ")))
cont=0
for i in range(0,3):
    for j in range(0,3):

        if (i==j): # nesse caso os indices tem que serem iguais
             cont=cont+mat[i][j]
             
print ("a soma eh: ",cont)













#Fazer um programa para ler os dados de uma
#matriz 3x3 e somar os elementos da diagonal
#principal
