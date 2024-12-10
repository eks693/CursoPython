# Projeto: Sistema Bancário com Interface Gráfica

## Descrição Geral
Este projeto implementa um sistema bancário simples utilizando **Python** com **Programação Orientada a Objetos (POO)** e uma interface gráfica criada com **Tkinter**. O sistema permite realizar operações básicas, como depósito, saque e consulta de saldo, além de gerincluir novas contas bancárias.

---

## Componentes do Sistema

### 1. Classe `ContaBancaria`
- Define uma conta bancária com métodos para:
  - **Depositar** valores.
  - **Sacar** valores.
  - **Mostrar o saldo disponível.**
- Implementa o **encapsulamento** para proteger o saldo da conta contra alterações externas indevidas.

### 2. Dicionário `contas`
- Utilizado para armazenar as instâncias da classe `ContaBancaria`, onde:
  - A **chave** é o número da conta.
  - O **valor** é a instância correspondente da conta.

### 3. Funções de Interface
- **`verificar_saldo()`**, **`depositar()`** e **`sacar()`**:
  - Permitem interagir com as contas bancárias utilizando os métodos da classe `ContaBancaria`.
  - São responsáveis por processar os dados da interface gráfica.

### 4. Interface Gráfica com `Tkinter`
- Cria uma janela interativa com os seguintes recursos:
  - Campos de entrada para o **número da conta** e o **valor da operação**.
  - Botões para:
    - **Verificar Saldo**
    - **Depositar**
    - **Sacar**

---

## Desafios Adicionais

### 1. Criação de Contas
- Implementar uma funcionalidade para criar novas contas diretamente pela interface gráfica.

### 2. Validações Extras
- Garantir que o valor inserido nas operações seja **positivo** e válido antes de processar a transação.

---

## Requisitos para Execução
- **Python 3.x** instalado no sistema.
- Biblioteca **Tkinter** (já incluída na instalação padrão do Python).

---

## Referências
- [Python Documentation](https://docs.python.org/3/)
- [Tkinter Documentation](https://docs.python.org/3/library/tkinter.html)
- [Programação Orientada a Objetos - Wikipedia](https://pt.wikipedia.org/wiki/Programa%C3%A7%C3%A3o_orientada_a_objetos)