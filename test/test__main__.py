import pytest
from calculadora.meu_pacote import Aula2modulo
from Curso.Senai.calculadora.meu_pacote import modulo_saudacao

def test_modulo_1():
    assert Aula2modulo.adicionar(1, 2) == 3
    assert Aula2modulo.subtrair(1, 2) == -1
    assert Aula2modulo.multiplicar(2, 2) == 4
    assert Aula2modulo.dividir(1, 2) == 0

def test_modulo_2():
    assert modulo_saudacao.escolha("Erick") == f"Olá, Escolha qual operação deseja?"
    assert modulo_saudacao.saudacao("Erick") == f"Olá, seja bem vindo!"
    assert modulo_saudacao.resposta("Erick") == f"A sua resposta da sua operação é: "
print(test_modulo_1)
print(test_modulo_2)
