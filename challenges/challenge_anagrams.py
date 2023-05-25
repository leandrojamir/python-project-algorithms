# 4 - Anagramas (Algoritmo de ordenação)
# O código deve ser feito dentro do arquivo challenges/challenge_anagrams.py.


def is_anagram(first_string, second_string):
    #  O algoritmo deve considerar letras maiúsculas e minúsculas como iguais
    # durante a comparação das entradas, ou seja, ser case insensitive.
    first_sort = my_sort(list(first_string.lower()))
    second_sort = my_sort(list(second_string.lower()))
    first = "".join(first_sort)
    second = "".join(second_sort)

    #  Faça um algoritmo que consiga comparar duas strings, ordená-las e
    # identificar se uma é um anagrama da outra. Ou seja, sua função irá
    # receber duas strings de parâmetro e o retorno da função será uma
    # tupla () com a primeira string ordenada, a segunda string ordenada e um
    # booleano, True ou False representando se são anagramas.
    # A função retorna False caso uma string não seja um anagrama da outra;
    if len(first_string) == 0 and len(second_string) == 0:
        return (first, second, False)
    #  A função retorna True caso uma string seja um anagrama da outra
    # independente se as letras são maiúsculas ou minúsculas;
    elif first == second:
        return (first, second, True)
    return (first, second, False)


# Você deverá implementar sua própria função de ordenação, ou seja, o
# uso de funções prontas não é permitido.
# Exemplos de funções não permitidas: sort, sorted e Counter;
# Não será permitido realizar nenhuma importação neste arquivo!
# https://www.programiz.com/dsa/selection-sort

#  AssertionError: Seu algoritmo parece ser O(n^2), mas deveria ser
# no máximo O(n log n)
#  assert False

# simplificar my_sort, dividir a lista em duas metades para ordenar e depois
# mesclar com merge_sort com objetivo de diminuir algoritimo quadratico
def my_sort(array):
    # se menor que 1 já vai estar ordenado automaticamente
    if len(array) <= 1:
        return array

    # dividir a lista na metade esquerda e direita
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    # vou chamar recursivamente até metade esquerda ou direita ser menor que 1
    left_half = my_sort(left_half)
    right_half = my_sort(right_half)

    #  depois merge para juntar as duas metades ordenadas e retornar o array
    # ordenado
    sorted_array = merge(left_half, right_half)
    return sorted_array


# https://www.alura.com.br/artigos/algoritmo-mergesort-implementar-python?gclid=CjwKCAjw67ajBhAVEiwA2g_jEIYhRTgU0RULuMF8zrNZIdAQHVi1BvPG0IxU4Ruyg41dYoWVtb-EaRoCY0AQAvD_BwE
def merge(left, right):
    result = []
    left_index, right_index = 0, 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        result.extend(left[left_index:])
    else:
        result.extend(right[right_index:])

    return result
