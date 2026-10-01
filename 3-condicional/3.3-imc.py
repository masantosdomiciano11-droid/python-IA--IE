nome = (input("digite seu nome: "))
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))


# cáculando o imc 
imc = peso / altura** 2 

# definindo situação secundo imc
if imc < 18.5:
    situacao = "abaixo do peso"
elif imc <= 24.9:
    situacao = "peso normal"
elif imc <= 29.9:
    situacao = "sobrepeso"
elif imc <= 34.9:
    situacao = "obesidade grau 1"
elif imc <= 39.9:
    situacao = "obesidade grau 2"
else:
    situacao = "obesidade grau 3"
print(f"o imc do paciente é {situacao}")
