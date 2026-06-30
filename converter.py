import requests
import tkinter as tk
from tkinter import ttk, messagebox

def converter():
    try:
        valor = float(entry_valor.get())
        origem = combo_origem.get().upper()
        destino = combo_destino.get().upper()

        url = f"https://api.frankfurter.app/latest?amount={valor}&from={origem}&to={destino}"
        resposta = requests.get(url)

        if resposta.status_code != 200:
            messagebox.showerror("Erro", "Não foi possível acessar a API.")
            return

        dados = resposta.json()
        resultado = dados["rates"][destino]
        label_resultado.config(text=f"{valor} {origem} = {resultado:.2f} {destino}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um problema: {e}")

# Lista de moedas comuns
moedas = ["USD", "EUR", "BRL", "GBP", "JPY", "AUD", "CAD"]

# Criar janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas 💱")
janela.geometry("320x250")

# Estilo moderno
style = ttk.Style()
style.theme_use("clam")

# Widgets
ttk.Label(janela, text="Valor:").pack(pady=5)
entry_valor = ttk.Entry(janela)
entry_valor.pack()

ttk.Label(janela, text="Moeda de origem:").pack(pady=5)
combo_origem = ttk.Combobox(janela, values=moedas)
combo_origem.set("BRL")
combo_origem.pack()

ttk.Label(janela, text="Moeda de destino:").pack(pady=5)
combo_destino = ttk.Combobox(janela, values=moedas)
combo_destino.set("USD")
combo_destino.pack()

btn_converter = ttk.Button(janela, text="Converter", command=converter)
btn_converter.pack(pady=10)

label_resultado = ttk.Label(janela, text="", font=("Arial", 12, "bold"), foreground="#007acc")
label_resultado.pack(pady=10)

# Rodar a interface
janela.mainloop()
