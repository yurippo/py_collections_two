import dictionary_variations_counter
from conta import Conta
from collections import Counter, defaultdict


#Now I'm gonna create some accounts
#Defaultdict super cool to perform tests

contas = defaultdict(Conta)
print(contas[15])

print(contas[17])

#defaultdict can be used as a word counter for example or a temporary cache than can be updated
#but if we know the API the documentation there's a Counter there already ready to use
#the standard Python API standard Python Documentation so I imported counter and used below

my_text ="Bem vindo meu nome e Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
my_lower_text = my_text.lower()
print(my_lower_text)

#What the counter is going to do? Count now my code has just one line problem resolved ;) it's in the standard Python Library
#That's Why it's very important to know how to use the language API we have the code there ready for us

aparicoes_contas = Counter(my_lower_text.split())

print(aparicoes_contas)