from collections import Counter, defaultdict


texto = "Bem vindo meu nome é Elias irei falar sobre os meus gostos eu gosto muito de cachorros e gatos eu gosto também de beber café"

texto = texto.lower()

# Conforme aprendemos no projeto, é possível fazer a contagem de palavras, utilizando o default dict e o Counter para contar valores.

# Como podemos contar as aparições de cada palavra da seguinte frase?

#First I will import counter and defaultdict from collections to help me solve this problem

conta_palavras = Counter(texto.split())
print(conta_palavras)

#Problem resolved with Counter
#Com o Counter nós estamos separando as letras e fazendo a contagem dos valores.
#Counter({'eu': 2, 'gosto': 2, 'de': 2, 'bem': 1, 'vindo': 1, 'meu': 1, 'nome': 1, 'é': 1, 'elias': 1, 'irei': 1, 'falar': 1, 'sobre': 1, 'os': 1, 'meus': 1, 'gostos': 1, 'muito': 1, 'cachorros': 1, 'e': 1, 'gatos': 1, 'também': 1, 'beber': 1, 'café': 1})

#Second I will resolved the issue using defaultdict
#Problem resolved with defaultdict
#Quando utilizamos o default dict é para fazer a criação de um dicionário. Usamos nesse caso um loop para criar o contador

conta_palavras_new = defaultdict(int)

for word in texto.split():
    conta_palavras_new[word] += 1

print(conta_palavras_new)


# defaultdict(<class 'int'>, {'bem': 1, 'vindo': 1, 'meu': 1, 'nome': 1, 'é': 1, 'elias': 1, 'irei': 1, 'falar': 1, 'sobre': 1, 'os': 1, 'meus': 1, 'gostos': 1, 'eu': 2, 'gosto': 2, 'muito': 1, 'de': 2, 'cachorros': 1, 'e': 1, 'gatos': 1, 'também': 1, 'beber': 1, 'café': 1})

# O que aprendemos neste projeto:

# Contar quantas vezes aparece uma palavra;
# Utilizar o default dict;
# Utilizar o Counter para contar valores.