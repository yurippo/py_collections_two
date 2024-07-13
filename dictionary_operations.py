aparicoes = {
    "Guilherme":1,
    "cachorro":2,
    "nome":2,
    "vindo":1
}


aparicoes["Carlos"] = 1

print(aparicoes)

aparicoes["Carlos"] = 2

print(aparicoes)

del aparicoes["Carlos"]
print(aparicoes)

print("cachorro" in aparicoes)

print("Carlos" in aparicoes)

#In is used to searche in the keys

#I iterate inside a dictionary using for loop

for elemento in aparicoes:
    print(elemento)

#That means aparicao is an iterate and returns the keys

#I can also do this way

for elemento in aparicoes.keys():
    print(elemento)

#That also gives me the same result

#But if I would like to iterate the values instead of the keys for example I can do it this way

for elemento in aparicoes.values():
    print(elemento)

#to check if 1 is in values I can do

print(1 in aparicoes.values())

#In the situation I wanna iterate the key and the value I can do this way

#common loops used with dictionaries

for elemento in aparicoes.keys():
    valor = aparicoes[elemento]
    print(elemento, valor)

for elemento in aparicoes.items():
    print(elemento)

for chave, valor in aparicoes.items():
    print(chave, "=",valor)

#I can also use list comprehension with dictionaries creating a list like below

palavra = ["palavra {}".format(chave) for chave in aparicoes.keys()]
print(palavra)

#O que aprendemos no projeto
# O que é um dicionário;
# Verificar se o elemento está dentro do dicionário;
# Utilizar o get para verificação;
# Criar um dicionário a partir do dict;
# Adicionar um elemento no dicionário;
# Remover um elemento do dicionário;
# Mostrar os elementos dentro do dicionário;
# Usar a função keys para pegar as chaves;
# Usar a função values para pegar os valores;
# Percorrer linha a linha com a função items