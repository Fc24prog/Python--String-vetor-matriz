def soma2(x,y):
    soma=0
    for i in range (x+1,y):
        if i%7==0:
            soma=soma+i

        if i %13==0:
            soma=soma-i
    
    return soma


a = int(input("N1:"))
b = int(input("N2:"))
print ("soma:", soma2(a,b))



#Fazer um módulo para receber dois valores inteiros
#e retornar a soma dos múltiplos de 7 MENOS a soma
#dos múltiplos de 13 ENTRE esses valores
