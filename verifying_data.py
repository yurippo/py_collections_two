# Fomos chamados para verificar os dados das pessoas que fizeram o curso de data science e machine learning, com a finalidade de identificar as pessoas que estão assistindo os dois cursos. Então vamos analisar o seguinte conjunto:

usuarios_data_science = {15, 23, 43, 56}

usuarios_machine_learning = {13, 23, 56, 42}

#Como podemos fazer a verificação dos dados?

usuarios_data_science_ml_combinados = (usuarios_data_science & usuarios_machine_learning)

print(usuarios_data_science_ml_combinados)

#result {56, 23}

#Quando utilizamos o & pegamos os números que estão em ambos conjuntos e mostramos

#O | faz a junção dos conjuntos

#O - é utilizado para fazer a remoção de elementos repetidos nos dois conjuntos

#Aprendemos o que sao sets conjuntos;
# Criar conjuntos;
# Utilizar o | para juntar conjuntos;
# Utilizar o & para juntar apenas números que estão no mesmo conjunto;
# Utilizar o - para remover números repetidos que estão nos dois conjuntos;
# O que é ou (^) exclusivo.