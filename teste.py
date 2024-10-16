import tkinter as tk
import time

def adicionar_numero(numero):
    valor_atual = entry.get()
    novo_valor = valor_atual + str(numero)
    entry.delete(0, tk.END)
    entry.insert(0, novo_valor)

def calcular(operacao):
    global primeiro_numero
    ultimo_operador = ""  # Initialize here within the function
    if primeiro_numero != "":
        if operacao:  # Se um operador foi passado
            num2 = float(entry.get())
            if operacao == "+":
                resultado = primeiro_numero + num2
            elif operacao == "-":
                resultado = primeiro_numero - num2
            # ... outras operações
            result_label.config(text=f"Resultado: {resultado}")
            entry.delete(0, tk.END)
            primeiro_numero = resultado  # Atualiza o primeiro número com o resultado
            ultimo_operador = operacao  # Armazena o último operador
        else:  # Se o botão "=" foi pressionado
            if ultimo_operador:
                num2 = float(entry.get())
                if ultimo_operador == "+":
                    resultado = primeiro_numero + num2
                # ... outros cálculos com o último operador
                result_label.config(text=f"Resultado: {resultado}")
                entry.delete(0, tk.END)
                primeiro_numero = resultado
    else:
        primeiro_numero = float(entry.get())
        entry.delete(0, tk.END)
primeiro_numero = ""  # Inicializar 'primeiro_numero' como vazia

root = tk.Tk()
root.title("Calculadora Simples")

entry = tk.Entry(root)
entry.grid(row=0, column=0, columnspan=4)

# Botões numéricos
for i in range(1, 10):
    button = tk.Button(root, text=str(i), command=lambda num=i: adicionar_numero(num))
    button.grid(row=(i-1)//3 + 1, column=(i-1)%3)

# Botão 0
button_0 = tk.Button(root, text="0", command=lambda: adicionar_numero(0))
button_0.grid(row=4, column=1)

result_label = tk.Label(root, text="Resultado:")
result_label.grid(row=5, column=0)

button_add = tk.Button(root, text="+", command=lambda: calcular("+"))
button_add.grid(row=0, column=4)
button_sub = tk.Button(root, text="-", command=lambda: calcular("-"))
button_sub.grid(row=1, column=4)
button_mul = tk.Button(root, text="*", command=lambda: calcular("*"))
button_mul.grid(row=0, column=5)
button_div = tk.Button(root, text="/", command=lambda: calcular("/"))
button_div.grid(row=1, column=5)

# Botão "="
button_igual = tk.Button(root, text="=", command=lambda: calcular(""))
button_igual.grid(row=2, column=4)

root.mainloop()