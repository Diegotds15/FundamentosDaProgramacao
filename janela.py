import tkinter as tk

janela = tk.Tk()

janela.title("Minha primeira janela!")
janela.geometry("800x600")
janela.configure(bg="lightblue")

rotulo = tk.Label(janela, text="Bem-vindo ao Tkinter!")
rotulo.pack()

# Adicionar um botão
def botao_clicado():
    print("Botão clicado!")

botao = tk.Button(janela, text="Clique aqui", command=botao_clicado)
botao.pack()

tk.Entry(janela).pack()

janela.mainloop()




# Iniciar o loop principal
janela.mainloop()