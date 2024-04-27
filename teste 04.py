mat=[]
for i in range (0,3):
   mat.append(0)
   mat[i]=[]
   for j in range (0,3):
        mat[i].append(int(input("Entre com o elemento: ")))
cont=0
for i in range(0,3):
    for j in range(0,3):

        if (mat[i][j]%2==0):

            cont=cont+mat[i][j]

print("a soma dos pares eh: ",cont)

tot=0

for i in range(0,3):
    for j in range(0,3):
    
            tot=tot+mat[i][j]

print("O total de linha é: ",tot)


#Fazer um programa para imprimir a soma das
#linhas de uma matriz 3x3, e a soma total dos
#elementos PARES da matriz
