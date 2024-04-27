def primo (num):
    cont = 0
    for i in range(2,num):
        if(num%i)==0:
            cont += 1
        if cont > 0:

            return False
        
        else:

            return True
        
#programa principal

x=int(input("Entre com o número: "))

if primo (x):
    
    print ("O numero eh primo: ")
    
else:
    
    print ("O numero NAO eh primo: ")
