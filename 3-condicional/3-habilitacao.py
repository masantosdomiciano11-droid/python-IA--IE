# solicitando o nome e a idade do usuário
nome = input("digite seu nome:marcos ")
idade = int(input("digite sua idade:13 "))

# criando a decisão caso for maior ou menor de 18 anos 
if idade >= 18:
    print("Maior de idade")
else:
    print("Menor de idade")