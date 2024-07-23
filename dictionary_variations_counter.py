from collections import defaultdict

#Now we gonna dive into the power of knowing the API and collections a programming langiage offers us

#No we're gonna try to simplify even more my previous defaultdict code

my_text ="Bem vindo meu nome e Guilherme eu gosto muito de nomes e tenho o meu cachorro e gosto muito de cachorro"
my_lower_text = my_text.lower()
print(my_lower_text)

aparicoes_new = defaultdict(int)

# for new_word in my_lower_text.split():
#     ate_entao = aparicoes_new[new_word]
#     aparicoes_new[new_word] = ate_entao +1

# print(aparicoes_new)

#New code below we have our new counter

for new_word in my_lower_text.split():
    ate_entao = aparicoes_new[new_word]
    aparicoes_new[new_word]+=1

print(aparicoes_new)

#the other power of the defaultdict is that we can use it with objects not only integers next code I'll create the class conta

#simplifying my code even more

aparicoes_new = defaultdict(int)

for palavra in my_lower_text.split():
    aparicoes_new[palavra] +=1

print(aparicoes_new)