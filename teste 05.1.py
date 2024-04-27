mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(int(input("Entre com o elemento: ")))
cont=0
for i in range(0,3):
    for j in range(0,3):

        if (i+j==3-1): # diagornal segundaria é: i+j=n-1, n é o tamanho da matriz
             cont=cont+mat[i][j]
             
print ("a soma eh: ",cont)











#Fazer um programa para apresentar a diagonal
#secundária de uma matriz 3x3
