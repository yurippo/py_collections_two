#Dictionary(Map,etc)
#Python Documentation
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries
#chave "Guilherme" valor 1

#most common way to create a dictionary
aparicoes = {
    "Guilherme":1,
    "Cachorro":2,
    "Nome":3,
    "Vinho":1
}

print(aparicoes)

#{'Guilherme': 1, 'Cachorro': 2, 'Nome': 3, 'Vinho': 1}

print(type(aparicoes))
#<class 'dict'>

print(aparicoes["Guilherme"])
#1

print(aparicoes["Cachorro"])
#2

#print(aparicoes["xpto"])
# Traceback (most recent call last):
#   File "c:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_collections_two\dictionary.py", line 27, in <module>
#     print(aparicoes["xpto"])
#           ~~~~~~~~~^^^^^^^^
# KeyError: 'xpto'

#To fix this error if I want to get a key that is 0 for example I can use the get method

print(aparicoes.get("xpto",0))
#0

print(aparicoes.get("Cachorro",0))
#actually returns 2 that is the value for Cachorro

#The dictionary gives us this advantage to be able to work key value, key value

#I could also create the dictionary in a second way example

aparicoes = dict(Guilherme = 2, cachorro = 1) #this is not the most common way
print(aparicoes)
#This way I also have adictionary
#{'Guilherme': 2, 'cachorro': 1}