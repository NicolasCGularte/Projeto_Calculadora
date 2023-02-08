from Classes import Calculadora, Arquivo

if __name__ == "__main__":
    calculadora = Calculadora()
    arquivo = Arquivo()

    print("Bem-vindo à calculadora em Python")
    print("Exemplos de operações: '2 + 2', '5 - 3', '4 * 2', '6 / 2', '3 ** 2'")

    while True:
        entrada = input("Digite a operação ou 's' para sair: ")
        if entrada == "s":
            break
        else:
            try:
                num1, operacao, num2 = entrada.split(" ")
                num1, num2 = int(num1), int(num2)
                # print(num1,num2)
            except ValueError:
                print("Erro: Insira uma operação válida.")
            else:
                if operacao == "+":
                    resultado = calculadora.soma(num1, num2)
                    operacao = "soma"
                elif operacao == "-":
                    resultado = calculadora.subtracao(num1, num2)
                    operacao = "subtração"
                elif operacao == "*":
                    resultado = calculadora.multiplicacao(num1, num2)
                    operacao = "multiplicação"
                elif operacao == "/":
                    resultado = calculadora.divisao(num1, num2)
                    operacao = "divisão"
                elif operacao == "**":
                    resultado = calculadora.potencia(num1, num2)
                    operacao = "potência"
                else:
                    print("Erro: Operação inválida.")
                    continue
            finally:
                print("Resultado:", resultado)
                arquivo.salvar_resultado(resultado, operacao)
