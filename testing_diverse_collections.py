
from collections import Counter

texto1 = """
essa é uma das famosas frases da obra Alice no país das maravilhas de Lewis Carroll que nos faz refletir sobre o quão necessário é saber onde queremos chegar para não optar por rumos ainda mais incertos.

Mas quando adaptamos esta reflexão para o mundo dos negócios, além de saber para onde ir, é necessário definir o “como” chegar lá, pois sem esta definição de processo há uma grande probabilidade de não chegar a lugar algum. É justamente neste ponto que a gestão de processos entra em ação.

A gestão de processos descreve como uma organização funciona, fazendo parte da cultura organizacional a nível de tarefa, departamento ou integralmente em relação ao negócio.
Nela, é possível esquematizar e documentar uma série de atividades encadeadas que geram um processo bem definido e, quando descrito e compreendido, garante um alinhamento entre todas as partes interessadas envolvidas nos objetivos que devem ser alcançados.
"""

texto2 = """
No desenvolvimento de software, a virtualização é como criar "cópias" do seu computador dentro do próprio computador. Imagine que você tem uma cozinha onde prepara diferentes tipos de comida.

Para não misturar os ingredientes, você cria estações separadas para cada receita.

A virtualização faz algo similar: cria espaços separados para que diferentes projetos de software possam ser desenvolvidos e testados sem interferir entre si.

Essa técnica é importante porque, no desenvolvimento de software, cada projeto pode ter suas próprias necessidades e dependências.

Usar a mesma "cozinha" para tudo poderia causar muitos problemas. Por exemplo, um projeto pode precisar de uma versão específica de uma biblioteca que não é compatível com outra versão usada em outro projeto… e aí teremos problemas, certo?

A virtualização permite que você tenha múltiplos ambientes, cada um configurado com as versões e dependências exatas que cada projeto precisa.

Além disso, a virtualização facilita a colaboração entre desenvolvedores. Se todos os membros da equipe usarem ambientes virtuais idênticos, será mais fácil compartilhar e testar o código sem se preocupar com diferenças na configuração dos computadores individuais.

Isso é como se todos na sua cozinha tivessem as mesmas ferramentas e ingredientes à disposição, garantindo que qualquer pessoa possa continuar a receita exatamente de onde outro parou, sem surpresas desagradáveis.

Mas como isso funciona em Python? O objetivo desse artigo é justamente explicar como usar Venv e Poetry no Python para criar e gerenciar ambientes virtuais de desenvolvimento

"""

def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    soma_total_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / soma_total_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print("{} => {:.2f}% ".format(caractere, proporcao*100))

analisa_frequencia_de_letras(texto1)

#Usando most_common passamos por parâmetro o número de elementos que queremos, no nosso caso foi 10. Ele vai nos retornar uma lista de tuplas com os elementos e suas devidas proporções.

# for letra, frequencia in aparicoes.items():
#     tupla = (letra,frequencia / soma_total_caracteres)
#     print(tupla)


#if I want to create a list I can use list comprehension



#print(proporcoes)

#print(mais_comuns)

# O que aprendemos neste projeto:

# Mostrar o quão frequente são as letras;
# Ver aparições de elementos e o total de aparições.