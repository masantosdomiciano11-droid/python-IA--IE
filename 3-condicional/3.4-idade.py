idade = (int(input("digite sua idade: ")))
nome = (input("digite seu nome: "))
# situação da idade
 
if idade <= 0 - 3:
    situacao = "bbzin"
elif idade < 4 - 10:
    situacao = "crinaça" 
elif idade < 11 - 14:
    situacao = "aborecente"
elif idade < 15 - 30:
    situacao = "jovente"
elif idade < 31 - 64:
    situacao = "adultero"
else:
    situacao = "mais mais"
print(f"o pacinete é {situacao}")