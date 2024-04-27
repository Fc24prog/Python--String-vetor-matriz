mat=[]
for i in range(0,3):
    mat.append(0)
    mat[i]=[]
    for j in range(0,3):
        mat[i].append(int(input("Entre com o elemento da 1ª matriz: ")))
cont=0
for i in range(0,3):
    for j in range(0,3):

        if (i==j): # nesse caso os indices tem que serem iguais
             cont=cont+mat[i][j]
             
print ("a mat1 eh: ",mat)

mat2=[]
for i in range(0,3):
    mat2.append(0)
    mat2[i]=[]
    for j in range(0,3):
        mat2[i].append(int(input("Entre com o elemento da 2ª matriz: ")))
cont2=0
for i in range(0,3):
    for j in range(0,3):

        if (i+j==3-1): # diagornal segundaria é: i+j=n-1, n é o tamanho da matriz
             cont2=cont2+mat[i][j]
             
print ("a mat 2  eh: ",mat2)

vet=[0]*3

for i in range (0,3):
    vet[i]=cont + cont2
    
print("O vetor é: ",vet)









#Fazer um programa para guardar a soma dos
#elementos da diagonal principal de uma matriz 3x3
#mais a soma dos elementos da diagonal secundária
#de uma outra matriz 3x3 em um vetor
