from collections import defaultdict

#https://docs.python.org/3/library/string.html

my_text ="Bem vindo meu nome e Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
my_lower_text = my_text.lower()
print(my_lower_text)


aparicoes = {}
for word in my_lower_text.split():
    ate_agora = aparicoes.get(word,0)
    aparicoes[word] = ate_agora +1

print(aparicoes)

#https://docs.python.org/3/library/collections.html

aparicoes_new = defaultdict(int)

for new_word in my_lower_text.split():
    ate_entao = aparicoes_new[new_word]
    aparicoes_new[new_word] = ate_entao +1

print(aparicoes_new)


