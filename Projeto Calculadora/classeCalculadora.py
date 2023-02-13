from Classes import Calculadora, Arquivo

if __name__ == "__main__":
    """
    Inicialização da classe Calculadora e Arquivo.
    """
    calculadora = Calculadora()
    arquivo = Arquivo()

    print("Bem-vindo à calculadora em Python")
    print("Exemplos de operações: '2 + 2', '5 - 3', '4 * 2', '6 / 2', '3 ** 2'")

while True:
    """
    Loop que recebe uma entrada do usuário e realiza as operações matemáticas.
    """
    entrada = input("Digite a operação ou 's' para sair: ")
    if entrada == "s":
        break
    else:
        try:
            """
            Tenta separar a entrada em 3 partes: número 1, operação e número 2.
            """
            num1, operacao, num2 = entrada.split(" ")
            num1, num2 = int(num1), int(num2)
        except ValueError:
            """
            Se a entrada não for válida, exibe mensagem de erro.
            """
            print("Erro: Insira uma operação válida.")
            continue
        else:
            """
            Verifica qual operação o usuário deseja realizar.
            """
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
                """
                Se a operação não for válida, exibe mensagem de erro.
                """
                print("Erro: Operação inválida.")
                continue
            """
            Exibe o resultado da operação.
            """
            print("Resultado:", resultado)
            arquivo.salvar_resultado(resultado, operacao)
