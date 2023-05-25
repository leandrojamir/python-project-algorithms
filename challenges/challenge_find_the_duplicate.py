# Requisitos Bônus
# 5 - Encontrando números repetidos (Algoritmo de busca)
#  Dada um array de números inteiros contendo n + 1 inteiros, chamado de nums,
# em que cada inteiro está no intervalo [1, n].
# Retorne apenas um número duplicado em nums.
#  Este requisito será testado executando milhares de vezes sobre várias
# entradas com o tamanho variável. Tais execuções no avaliador irão determinar
# de maneira empírica, através de cálculos, a complexidade assintótica do seu
# algoritmo.
#  O tempo de execução do código na sua máquina pode variar em relação ao
# avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo
# de execução. Ainda assim, o que vale é o resultado do avaliador, e não o
# local. Na dúvida, busque ajuda do time de instrução;
# O código deve ser feito dentro do arquivo challenge_find_the_duplicate.py.
def find_duplicate(nums):
    # O array montado deve:
    #  Ter apenas um único número repetindo duas ou mais vezes, todos os outros
    # números devem aparecer apenas uma vez;
    #  Ter, no mínimo, dois números.
    # https://stackoverflow.com/questions/9835762/how-do-i-find-the-duplicates-in-a-list-and-create-another-list-with-them
    # seen = set()
    # dupes = []
    # for x in a:
    #     if x in seen:
    #         dupes.append(x)
    #     else:
    #         seen.add(x)
    viewed = set()
    for num in nums:
        # TypeError: '<' not supported between instances of 'str' and 'int'
        # 5.3 - Retorne False se a função receber, como parâmetro, uma string
        if isinstance(num, str):
            return False
        #  Ter apenas números inteiros positivos maiores do que 1;
        if num < 0:
            return False
        # Se o número já foi visto, significa que é um duplicado e é retornado.
        if num in viewed:
            return num
        # Caso contrário, adiciona o número ao conjunto dos numeros vistos.
        viewed.add(num)
    #  Caso não passe nenhum valor ou uma string ou não houver números
    # repetidos retorne False;
    return False
