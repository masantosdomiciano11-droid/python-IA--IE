
lisita_inicial = ["joão","pamela","dominique"]

print("lista_inicial: ",lisita_inicial)

print(60 * "-")

lisita_inicial.append("eduarda")
#========acrecentando item na lsita========
print("após o append",lisita_inicial)
print(60 * "-")
#========acrecentando item na lsita(específica)========
lisita_inicial.insert(2,"matheus")

print("após o insert()",lisita_inicial)
print(60 * "-")

#=========modificando item em uma lista==========
lisita_inicial[3] = "rafael"
print("após modificação: ",lisita_inicial)
print(60 * "-")

#==============apagando item em índice específico===========
del lisita_inicial[3]
print("após del: ",lisita_inicial)
print(60 * "-")

#=========modificando item em uma lista==========
lisita_inicial.remove("pamela")

print("após remove: ",lisita_inicial)
print(60 * "-")


removiod = lisita_inicial.pop(1)

print(f"após pop, removido {removiod}", lisita_inicial)


