def somaMult(x,y):
    soma = 0
    for i in range(x+1, y):
        if i % 7 == 0:
            soma += i

        if i % 13 == 0:
            soma -= i
        return soma

a = int(input("N1:"))
b = int(input("N2:"))
print ("soma:", somaMult(a,b))
