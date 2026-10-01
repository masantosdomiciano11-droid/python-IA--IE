# criando a função nome completo 
def nome_completo(nome,sobrenome):
    return f"{nome} {sobrenome}"

nome_usuario = ("digite seu nome: ")
sobrenome_usuario = ("digite seu sobrenome:")


nome_inteiro = nome_completo(nome_usuario,sobrenome_usuario)

print(f"welcome, {nome_inteiro}")