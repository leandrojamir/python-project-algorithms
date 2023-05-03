# 2 - Criptografia de inversões (Testes)
# Implemente em: tests/encrypt/test_encrypt.py
#  Durante a dinâmica em grupos de um processo seletivo, a empresa contratante
# definiu um desafio em duplas, e cada pessoa terá um papel. A primeira pessoa
# deve criar uma função de criptografia, e a segunda pessoa deve implementar
# os testes da função implementada pela primeira pessoa.
#  Você fará o papel da segunda pessoa nessa dinâmica, ou seja: deve
# implementar os testes de uma função de criptografia.
#  Esse teste deve se chamar test_encrypt_message, e ele deve garantir que a
# função de criptografia encrypt_message deve respeitar uma lógica específica.
from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    # Recebe uma string message e um inteiro key como parâmetros
    #  Se key e message não possuírem os tipos corretos, uma exceção deve
    # ser lançada result = TypeError
    with pytest.raises(TypeError):
        encrypt_message(key="string", message="leandro")
    with pytest.raises(TypeError):
        encrypt_message(key=1, message=123)

    #  Se key não for um índice positivo válido de message, retorna a string
    # message invertida
    assert encrypt_message(key=-1, message="leandro") == "ordnael"
    # Se key for ímpar:
    # divide message no índice key, inverte os caracteres de cada parte, e
    # retorna a união das partes novamente com "_" entre elas
    assert encrypt_message(key=1, message="leandro") == "l_ordnae"
    # Se key for par:
    # divide message no índice key, inverte a posição das partes, inverte os
    # caracteres de cada parte, e retorna a união das partes novamente
    # com "_" entre elas
    assert encrypt_message(key=4, message="leandro") == "ord_nael"
