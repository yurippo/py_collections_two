# Filtrando valores

# Sérgio precisa implementar um dicionário que tenha o nome e a idade de seus clientes, para saber a faixa etária deles. Esta implementação terá mil registros. Após cadastrá-los, ele deve verificar alguns clientes existentes no dicionário.

# Como ele pode fazer isto?

nome_idade = {
    "Sergio":30,
    "Carla":20,
    "Guilherme":40
}

print("Yuri" in nome_idade.keys())

#Um outra forma seria Utilizar a função GET, verificando se o cliente está contido no dicionário

print(nome_idade.get("Yuri"))