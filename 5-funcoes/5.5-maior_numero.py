# criando função maior número

def maior_numero(x,y):
    if x > y:
        return x

    else:
        return y
# solicitando os números 
numero_1 = float(input("digite um númro: "))
numero_2 = float(input("digite um numero: "))
# apresentando o resultado do maior número
resultado = maior_numero(numero_1,numero_2)
print(resultado)