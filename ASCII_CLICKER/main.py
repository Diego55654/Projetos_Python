import tkinter as tk
import pyfiglet #type:ignore

# Função que mostra o texto aos poucos
def mostrar_parcial(ascii_text, i=0):
    # Limpa e insere apenas até o índice atual
    text_widget.delete(1.0, tk.END)
    text_widget.insert(tk.END, ascii_text[:i])

    # Se ainda não chegou ao fim, agenda a próxima chamada
    if i < len(ascii_text):
        root.after(30, lambda: mostrar_parcial(ascii_text, i+1))

# Função chamada pelo botão
def gerar_ascii():
    texto = "Diego, o milhor"
    ascii_text = pyfiglet.figlet_format(texto)
    mostrar_parcial(ascii_text, 0)

# Janela principal
root = tk.Tk()
root.title("ASCII Converter")

# Botão
button = tk.Button(root, text="Generate ASCII Art", width=20, height=2, command=gerar_ascii)
button.configure(bg="black", fg="white", font=("Helvetica", 12, "bold"))
button.pack(pady=10)

# Área de texto para mostrar ASCII
text_widget = tk.Text(root, width=80, height=20, font=("Courier", 10))
text_widget.pack(padx=10, pady=10)

root.mainloop()
