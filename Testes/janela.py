import tkinter as tk

janela = tk.Tk()

janela.title("Gay gay!")
janela.geometry("800x600")
janela.configure(bg="lightblue")

rotulo = tk.Label(janela, text="Thiago gay!", font=("Arial", 50))
rotulo.configure(bg="red")
rotulo.pack()

# Adicionar um botão
def botao_clicado():
    texto1 = tk.Label(janela, text="KAKAKA", font=("Arial", 50))
    texto1.configure(bg="blue")
    texto1.pack()
    tk.Entry(janela, font=("Arial", 50)).pack()
    

botao = tk.Button(janela, text="Clique aqui", command=botao_clicado)
botao.pack()

# Iniciar o loop principal
janela.mainloop()