import requests
import tkinter as tk
from tkinter import messagebox

def converter():
    try:
        valor = float(entry_valor.get())
        origem = entry_origem.get().upper()
        destino = entry_destino.get().upper()

        url = f"https://api.frankfurter.app/latest?amount={valor}&from={origem}&to={destino}"
        resposta = requests.get(url)

        if resposta.status_code != 200:
            messagebox.showerror("Erro", "Não foi possível acessar a API.")
            return

        dados = resposta.json()
        resultado = dados["rates"][destino]
        label_resultado.config(text=f"{valor} {origem} = {resultado:.2f} {destino}")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um problema: {e}")

# Criar janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas 💱")
janela.geometry("300x200")

# Widgets
tk.Label(janela, text="Valor:").pack()
entry_valor = tk.Entry(janela)
entry_valor.pack()

tk.Label(janela, text="Moeda de origem (ex: BRL):").pack()
entry_origem = tk.Entry(janela)
entry_origem.pack()

tk.Label(janela, text="Moeda de destino (ex: USD):").pack()
entry_destino = tk.Entry(janela)
entry_destino.pack()

btn_converter = tk.Button(janela, text="Converter", command=converter)
btn_converter.pack(pady=10)

label_resultado = tk.Label(janela, text="")
label_resultado.pack()

# Rodar a interface
janela.mainloop()
