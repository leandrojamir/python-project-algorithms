# 6 - Palíndromos (Iteratividade)
#  Resolva o mesmo problema apresentado no requisito 2 - Palíndromos, porém
# dessa vez utilizando a solução iterativa.
#  Este requisito será testado executando milhares de vezes sobre várias
# entradas com o tamanho variável. Tais execuções no avaliador irão determinar
# de maneira empírica, através de cálculos, a complexidade assintótica do seu
# algoritmo.
#  O tempo de execução do código na sua máquina pode variar em relação ao
# avaliador, mas o cálculo será feito em cima do comportamento, e não do tempo
# de execução. Ainda assim, o que vale é o resultado do avaliador, e não o
# local. Na dúvida, busque ajuda do time de instrução;
# O algoritmo deve utilizar a solução iterativa;
# O código deve ser feito dentro do arquivo challenge_palindromes_iterative.py.
def is_palindrome_iterative(word):
    #  6.4 - A função deverá, por meio de análise empírica, se comportar
    # (no avaliador remoto em sua Pull Request) como no máximo O(n), ou seja,
    # com complexidade assintótica linear.
    #  6.3 - Retorne False se nenhuma palavra for passada como parâmetro,
    # executando uma função iterativa ;
    if word == "":
        return False
    # https://www.edureka.co/blog/python-program-to-check-palindrome/
    # string=input(("Enter a string:"))
    # if(string==string[::-1]):
    #       print("The string is a palindrome")
    # else:
    #       print("Not a palindrome")
    inverted_word = word[::-1]
    #  6.1 - Retorne True se a palavra passada como parâmetro for um
    # palíndromo, executando uma função iterativa;
    if inverted_word == word:
        return True
    #  6.2 - Retorne False se a palavra passada como parâmetro não for um
    # palíndromo, executando uma função iterativa;
    else:
        return False
