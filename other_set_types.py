users = {1,5,76,34,52,13,17}

print(len(users))

#A set in Python is mutable by standard

users.add(13)

print(len(users))


users.add(765)

print(len(users))

#If we wanna use a set that is imutable in Python we congela the set we use the Frozen Set option 

frozen_set_users = frozenset(users)

print(frozen_set_users)

print(type(frozen_set_users))

#If I try to add something to the Frozenset it will throw me an error example

# frozen_set_users.add(766)

# frozenset({1, 34, 5, 76, 13, 17, 52, 765})
# <class 'frozenset'>
# Traceback (most recent call last):
#   File "c:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_collections_two\other_set_types.py", line 26, in <module>
#     frozen_set_users.add(766)
#     ^^^^^^^^^^^^^^^^^^^^
# AttributeError: 'frozenset' object has no attribute 'add'
# PS C:\Users\marci\OneDrive\AREA DE TRABALHO 2022-01-10\py_collections_two> 

#That means frozensets are imutable data sets

my_text = "welcome my name is Yuri and I like a lot names and I have my dog and I like a lot dogs"
my_split_text = my_text.split()
print(my_split_text)

#Result - ['welcome', 'my', 'name', 'is', 'Yuri', 'and', 'I', 'like', 'a', 'lot', 'names', 'and', 'I', 'have', 'my', 'dog', 'and', 'I', 'like', 'a', 'lot', 'dogs']

#so now I can create a set

my_split_text_set = set(my_split_text)
print(my_split_text_set)

#Result {'names', 'and', 'have', 'name', 'a', 'is', 'welcome', 'lot', 'my', 'I', 'dog', 'Yuri', 'like', 'dogs'}
#that means it removed the duplicates, spaces it's now almost like a dictionary

# O que aprendemos no projeto:

# Modificar o conjunto em tempo real;
# Congelar o conjunto com o frozenset;
# Tirar a duplicidade de uma String;
# Adicionar elementos no conjunto.

