def calculadora():
    print("Bem-vindo à calculadora em Python")
    print("Selecione o número da operação desejada:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Sair")

    escolha = int(input("Digite escolha(1/2/3/4/5): "))

    if escolha == 1:
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 + num2
        print("Resultado da adição:", resultado)
    elif escolha == 2:
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)
    elif escolha == 3:
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)
    elif escolha == 4:
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)
    elif escolha == 5:
        print("Saindo da calculadora...")
        exit()
    else:
        print("Opção inválida. Tente novamente.")

calculadora()