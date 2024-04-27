c=input("Entre com a frase: ")
cont=0
for i in range (len(c)-1 ,-1,-1):
    cont=cont+c[i]
print(cont)


















#Um palíndromo é uma cadeia que pode ser lida de frente para trás e de trás para
#frente. Ex: ‘SOMOS’ ‘1234321’. Implemente a função palindromo(palavra). O
#parâmetro palavra é uma string. A função deverá retornar True se for um palíndromo e
#alse caso contrário.
