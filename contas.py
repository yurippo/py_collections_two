from conta import Conta
from collections import defaultdict


#Now I'm gonna create some accounts
#Defaultdict super cool to perform tests

contas = defaultdict(Conta)
print(contas[15])

print(contas[17])

#defaultdict can be used as a word counter for example or a temporary cache than can be updated
#but if we know the API the documentation there's a Counter there already ready to use
#the standard Python API standard Python Documentation