n=int(input("Entre com a quantidade de alunos: "))

nt=[0.0]*n

soma=0
cont = 0

for i in range (0,n):

    nt[i]=float(input("Entre com as notas: "))
    soma= soma + nt[i]
    md= soma/n

for i in range (0,n):

              if nt[i]>md:
                  cont = cont + 1
              

print("a média eh: ",md)
print("Acima da média",cont)

#Criar um programa que lê as notas de uma turma de N alunos, e indica o
#número de alunos acima da média
