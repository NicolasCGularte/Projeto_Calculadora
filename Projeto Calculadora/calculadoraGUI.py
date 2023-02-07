import tkinter as tk

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora em Python")

        self.label = tk.Label(self.master, text="Selecione a operação desejada:")
        self.label.pack()

        self.add_button = tk.Button(self.master, text="Adição", command=self.add)
        self.add_button.pack()

        self.subtract_button = tk.Button(self.master, text="Subtração", command=self.subtract)
        self.subtract_button.pack()

        self.multiply_button = tk.Button(self.master, text="Multiplicação", command=self.multiply)
        self.multiply_button.pack()

        self.divide_button = tk.Button(self.master, text="Divisão", command=self.divide)
        self.divide_button.pack()

        self.quit_button = tk.Button(self.master, text="Sair", command=self.quit)
        self.quit_button.pack()

    def add(self):
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 + num2
        print("Resultado da adição:", resultado)

    def subtract(self):
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 - num2
        print("Resultado da subtração:", resultado)

    def multiply(self):
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 * num2
        print("Resultado da multiplicação:", resultado)

    def divide(self):
        num1 = float(input("Digite primeiro número: "))
        num2 = float(input("Digite segundo número: "))
        resultado = num1 / num2
        print("Resultado da divisão:", resultado)

    def quit(self):
        print("Saindo da calculadora...")
        self.master.quit()

def main():
    root = tk.Tk()
    calculadora = CalculadoraGUI(root)
    root.mainloop()

if __name__ == '__main__':
    main()
    