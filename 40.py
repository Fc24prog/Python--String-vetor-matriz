#Fazer um programa para ler uma STRING e imprimir
#a quantidade de VOGAIS

c = input('entre com uma cadeia: ')
cont = 0
for i in range(0,len(c)):
    if c[i] == 'a' or c[i] == 'e' or c[i] == 'i' or c[i] == 'o'or c [i] == 'u':
        cont+=1

print ('QTD: ', cont)
  
