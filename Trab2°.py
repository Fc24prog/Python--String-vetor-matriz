#ao inves de eu usar as letras, usei uma matriz mesmo. Uma matriz 3x3 de a1 até c3 colocando em formula de matriz da para ver
#a ordem de linha e de coluna certinho 


def determinante_D(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz)):
            
        
            diagona_principal = matriz[0][0]*matriz[1][1]*matriz[2][2]
            diagonal_secundaria=matriz[0][1]*matriz[1][2]*matriz[2][0]
            diagonal_terciaria=matriz[0][2]*matriz[1][0]*matriz[2][1]

            diagona_principal_oposta = matriz[0][2]*matriz[1][1]*matriz[2][0]
            diagonal_secundaria=matriz[0][0]*matriz[1][2]*matriz[2][1]
            diagonal_terciaria=matriz[0][1]*matriz[1][0]*matriz[2][2]

            determinante =((diagonal_principal)+(diagonal_secundaria)+(diagonal_terciaria)) -\
                   \ (diagonal_principal_oposta) - (diagonal_secundaria_oposta)-(diagonal_terciaria_oposta)

     return determinante 
def determinateX (d1,b1,c1,d2,b2,c2,d3,b3,c3):
    
    detX= d1*(b2*c3-c2*b3)- b1*(d2*c3-c2*d3)-c1*(a2*b3-b2*d3)

    return detX

def determinanteY(d1,a1,c1,d2,a2,c2,d3,a3,c3):
    
    detY= a1*(d2*c3-c2*d3)-b1*(a2*c3-c2*a3)-c1*(a2*d3-d2*a3)

    return detY

def determinanteZ(d1,a1,b1,d2,a2,b2,d3,a3,b3):
    
    detZ = a1*(b2*d3-d2*b3)-b1*(a2*d3-d2*a3)-d1(a2*b3-b2*a3)

    return detZ

a1=int(input("Entre com o valor de a1: "))
a2=int(input("Entre com o valor de a2: "))
a3=int(input("Entre com o valor de a3: "))
b1=int(input("Entre com o valor de b1: "))
b2=int(input("Entre com o valor de b2: "))
b3=int(input("Entre com o valor de b3: "))
c1=int(input("Entre com o valor de c1: "))
c2=int(input("Entre com o valor de c2: "))
c3=int(input("Entre com o valor de c3: "))
d1=int(input("Entre com o valor de d1: "))
d2=int(input("Entre com o valor de d2: "))
d3=int(input("Entre com o valor de d3: "))

rx=determinanteX(d1,b1,c1,d2,b2,c2,d3,b3,c3)/determinante_D(matriz)
ry=determinanteY(d1,a1,c1,d2,a2,c2,d3,a3,c3)/determinante_D(matriz)
rz=determinanteZ(d1,a1,b1,d2,a2,b2,d3,a3,b3)/determinante_D(matriz)


print("O valor de X eh: ", rx)

print("O valor de Y eh: ", ry)

print("O valor de Z eh: ", rz)



