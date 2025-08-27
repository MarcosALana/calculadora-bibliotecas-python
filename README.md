# Calculadora de Datas e Cálculos Matemáticos em Python

Programa em Python que utiliza **bibliotecas** para realizar cálculos avançados:  
- **`datetime`**: calcular quantos dias faltam para o Ano Novo.  
- **`math`**: calcular raiz quadrada e potência de números.  

## 🚀 Código principal
```python
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

O que foi aprendido
Importação de bibliotecas (import, from ... import).
Uso de datetime para manipulação de datas.
Uso de math para cálculos avançados (raiz, potência, pi, etc.).
Criação de menus integrando diferentes funcionalidades.

💭 Comentário pessoal

Gostei muito de usar bibliotecas em Python.
Percebi como elas ampliam o que posso fazer sem precisar reinventar a roda.
Agora já consigo criar programas mais práticos e úteis para o dia a dia.
