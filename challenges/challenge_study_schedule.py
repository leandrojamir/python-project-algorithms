# 1 - Número de estudantes estudando no mesmo horário (Algoritmo de busca)
#  Você trabalha na maior empresa de educação do Brasil. Certo dia, a pessoa
# Product Manager (PM) quer saber qual horário tem a maior quantidade de
# pessoas estudantes acessando o conteúdo da plataforma. Com esse dado em
# mãos, a pessoa PM saberá qual é o melhor horário para disponibilizar os
# materiais de estudo para ter o maior engajamento possível.
#  O horário de entrada e saída do sistema é cadastrado no banco de dados toda
# vez que uma pessoa estudante entra e sai do sistema. Esses dados estarão
# contidos em uma lista de tuplas (permanence_period) em que cada tupla
# representa o período de permanência de uma pessoa estudante no sistema com
# seu horário de entrada e de saída.
#  Seu trabalho é descobrir qual o melhor horário para disponibilizar os
# conteúdos de estudo. Para isso, utilize a estratégia de resolução de
# problemas chamada força bruta em que a função desenvolvida por você será
# chamada várias vezes com valores diferentes para a variável target_time e
# serão analisados os retornos da função.

# exemplo.
# Nos arrays temos 6 estudantes
# estudante             1       2       3       4       5       6
# permanence_period = [(2, 2), (1, 2), (2, 3), (1, 5), (4, 5), (4, 5)]
#  target_time = 5  # saída: 3, pois a quarta, a quinta e a sexta pessoa
# estudante ainda estavam estudando nesse horário.
# (contou 3 pessoas)
#  target_time = 4  # saída: 3, pois a quinta e a sexta pessoa estudante
# começaram a estudar nesse horário e a quarta ainda estava estudando.
#  target_time = 3  # saída: 2, pois a terceira e a quarta pessoa estudante
# ainda estavam estudando nesse horário.
#  target_time = 2  # saída: 4, pois a primeira, a segunda, a terceira e a
# quarta pessoa estudante estavam estudando nesse horário.
#  target_time = 1  # saída: 2, pois a segunda e a quarta pessoa estudante
# estavam estudando nesse horário.
# Para esse exemplo, depois de rodar a função para todos esses `target_times`,
# julgamos que o melhor horário é o `2`, pois esse retornou `4`, já que 4
# estudantes estavam presentes nesse horário!


def study_schedule(permanence_period, target_time):
    #  Dica: O melhor horário será aquele no qual o contador
    # retornado pela função for o maior
    contador = 0
    try:
        for entrada, saida in permanence_period:
            if entrada <= target_time <= saida:
                contador += 1

        return contador

    #  Caso o target_time passado seja nulo, o valor retornado pela função deve
    # ser None (considere o horário 0 como um horário válido);
    # Retorne None se em permanence_period houver alguma entrada inválida;
    except (TypeError):

        return None

#  O código deve ser feito dentro do arquivo
# challenges/challenge_study_schedule.py.


# tests/test_study_schedule.py::
# test_study_schedule_success[permanence_periods0-5-3] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_success[permanence_periods1-1-2] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_success[permanence_periods2-3-2] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_success[permanence_periods3-1-1] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_success[permanence_periods4-2-3] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_invalid_permanence_periods[permanence_periods0-5] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_invalid_permanence_periods[permanence_periods1-1] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_invalid_permanence_periods[permanence_periods2-3] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_invalid_permanence_periods[permanence_periods3-1] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_invalid_permanence_periods[permanence_periods4-2] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_empty_target_time[permanence_periods0] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_empty_target_time[permanence_periods1] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_empty_target_time[permanence_periods2] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_empty_target_time[permanence_periods3] PASSED
# tests/test_study_schedule.py::
# test_study_schedule_empty_target_time[permanence_periods4] PASSED
