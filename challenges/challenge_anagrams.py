# 4 - Anagramas (Algoritmo de ordenação)
# O código deve ser feito dentro do arquivo challenges/challenge_anagrams.py.


def is_anagram(first_string, second_string):
    #  O algoritmo deve considerar letras maiúsculas e minúsculas como iguais
    # durante a comparação das entradas, ou seja, ser case insensitive.
    first_sort = my_sort(list(first_string.lower()))
    second_sort = my_sort(list(second_string.lower()))
    # print(f"\nvvv\nprimeira string: {first_sort}")
    # primeira string: ['a', 'd', 'e', 'p', 'r']
    first = "".join(first_sort)
    print(f"\nvvv\nprimeira string: {first}")
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
def my_sort(array):
    size = len(array)
    for index in range(size - 1):
        min_index = index

        for info in range(index + 1, size):
            if array[info] < array[min_index]:
                min_index = info

        array[index], array[min_index] = (array[min_index], array[index])

    return array
