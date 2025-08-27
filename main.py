# Dia 10 - Datas e Cálculos Matemáticos

import math
from datetime import date

print("=== Calculadora de Datas e Números ===")

while True:
    print("\n1 - Quantos dias faltam para o Ano Novo?")
    print("2 - Raiz quadrada de um número")
    print("3 - Potência de um número")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        hoje = date.today()
        ano_novo = date(hoje.year + 1, 1, 1)
        diferenca = ano_novo - hoje
        print(f"Faltam {diferenca.days} dias para o Ano Novo.")
    elif opcao == "2":
        num = float(input("Digite um número: "))
        print(f"A raiz quadrada de {num} é {math.sqrt(num)}")
    elif opcao == "3":
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        print(f"{base} elevado a {expoente} é {math.pow(base, expoente)}")
    elif opcao == "0":
        print("Encerrando o programa. Até logo!")
        break
    else:
        print("Opção inválida!")
