import tkinter as tk

class CalculadoraGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Calculadora")

        self.display = tk.Entry(self.master, width=30, borderwidth=5)
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Botões numéricos
        self.create_button("1", 1, 1)
        self.create_button("2", 1, 2)
        self.create_button("3", 1, 3)
        self.create_button("4", 2, 1)
        self.create_button("5", 2, 2)
        self.create_button("6", 2, 3)
        self.create_button("7", 3, 1)
        self.create_button("8", 3, 2)
        self.create_button("9", 3, 3)
        self.create_button("0", 4, 2)

    def create_button(self, text, row, column):
        button = tk.Button(self.master, text=text, padx=40, pady=20, command=lambda: self.button_click(text))
        button.grid(row=row, column=column)

    def button_click(self, text):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, str(current) + str(text))

root = tk.Tk()
calculator = CalculadoraGUI(root)
root.mainloop()