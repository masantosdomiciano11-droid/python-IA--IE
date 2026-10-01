nome = (input("digite seu nome: "))
nota_1 = float(input("digite primeira nota: "))
nota_2 = float(input("digite segunda  nota: "))
nota_3 = float(input("digite terceira nota: "))
# realizando cálculo
media = (nota_1 + nota_2 + nota_3) / 3

print(f"A média do aluno(a) {nome} é {media} ")

if media < 4:
    print("reprovado")
elif media <= 6:
    print("recuperação")
else:
    print("aprovado")
        
