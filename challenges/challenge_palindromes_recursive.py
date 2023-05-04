# 3 - Palíndromos (Recursividade)
# Escreva uma função que irá determinar se uma palavra é um palíndromo ou não.
#  A função irá receber uma string de parâmetro e o retorno será um booleano,
# True ou False.
# Mas o que é um palíndromo?
#  Um palíndromo é uma palavra, frase ou número que mantém seu sentido mesmo
# sendo lido de trás para frente. Por exemplo, "ABCBA".
#  Neste projeto iremos focar somente em palavras palíndromas e não em frases
# ou números.

# Exemplo:
# word = "ANA"
# # saída: True
# word = "SOCOS"
# # saída: True
# word = "REVIVER"
# # saída: True
# word = "COXINHA"
# # saída: False
# word = "AGUA"
# # saída: False


# Não se preocupe com a análise da complexidade desse algoritmo;
# O código deve ser feito dentro do arquivo
# challenges/challenge_palindromes_recursive.py.
def is_palindrome_recursive(word, low_index, high_index):
    # Se for passado uma string vazia, retorne False;
    if word == "":
        return False

    # O algoritmo deve ser feito utilizando a solução recursiva;
    # https://www.youtube.com/watch?v=66ugH75ao7c
    if low_index >= high_index:
        return True
    # if word[0] != word[-1]:
    else:
        # reduzir o intervalo de caracteres a serem comparados a cada chamada.
        return word[low_index] == word[high_index] and is_palindrome_recursive(
            word, low_index + 1, high_index - 1
        )
