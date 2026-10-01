# criando a função verificar_idade
def verificar_idade(idade):
    if idade >= 18:
        return "maior de idade"
    else:
        return "menor de idade"
# solicitando a idade do usuario
idade_usuario = int(input("digite sua idade: "))
resultado = verificar_idade(idade_usuario)

print(resultado)