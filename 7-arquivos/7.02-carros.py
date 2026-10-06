import csv

dados_tabela = [
    ["BAIRRO","CIDADE","ESTADO","CEP"],
    ["jardim cruzeiro","itapevi","sp","06680670"],
    ["parque santana","santana de parnaíba","sp","066548756"],
    ["suburbano","itapevi","sp","066435687"],
    ["centro","jandira","sp","066254789"]
]

with open("7.02-cidades.csv","w",encoding="utf-8",newline="") as arquivo_csv:
    escrevendo = csv.writer(arquivo_csv)
    escrevendo.writerow(dados_tabela)

