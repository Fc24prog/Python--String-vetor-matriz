def soma(x,y): # nome da função

    s=x+y # parametro da função
    
    return s

# ou podemos colocar a soma no return.

   #return x+y

#prog. principal

a=float(input("Entre coom o 1ª numero: "))
b=float(input("Entre coom o 2ª numero: "))

res= soma(a,b) # "a" se tornou x e "b" y

print("A soma dos numeros sao: ",res)

# podemos colocar também a conta da função para apresentar dentro do print

#print ("A soma dos numeros sao: ",soma(a,b))

