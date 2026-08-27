import requests
import tkinter as tk
from tkinter import ttk, messagebox

def converter():
    try:
        valor = float(entry_valor.get())
        origem = combo_origem.get().upper()
        destino = combo_destino.get().upper()
        
        if origem == destino:
            label_resultado.config(text=f"{valor} {origem} = {valor:.2f} {destino}")
            return

        url = f"https://api.frankfurter.app/latest?amount={valor}&from={origem}&to={destino}"
        resposta = requests.get(url)

        if resposta.status_code != 200:
            messagebox.showerror("Erro", "Não foi possível obter dados da API (status code diferente de 200).")
            return

        dados = resposta.json()
        resultado = dados["rates"][destino]
        label_resultado.config(text=f"{valor} {origem} = {resultado:.2f} {destino}")
    except ValueError:
        messagebox.showerror("Erro", "Digite um valor numérico válido.")
    except requests.exceptions.RequestException:
        messagebox.showerror("Erro de Conexão", "Não foi possível conectar à API. Verifique sua conexão com a internet.")
    except KeyError:
        messagebox.showerror("Erro", "Moeda não suportada ou problema nos dados recebidos.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um problema inesperado: {e}")

# Lista de moedas comuns
moedas = ["USD", "EUR", "BRL", "GBP", "JPY", "AUD", "CAD"]

# Criar janela principal
janela = tk.Tk()
janela.title("Conversor de Moedas 💱")
janela.geometry("350x360")
janela.resizable(False, False)

# Estilo moderno
style = ttk.Style()
style.theme_use("clam")

# Frame principal com padding
frame = ttk.Frame(janela, padding="20 20 20 20")
frame.pack(fill="both", expand=True)

# Widgets
ttk.Label(frame, text="Valor:", font=("Arial", 10)).pack(pady=(0, 5))
entry_valor = ttk.Entry(frame, font=("Arial", 10), justify="center")
entry_valor.pack(fill="x", pady=(0, 15))

ttk.Label(frame, text="Moeda de origem:", font=("Arial", 10)).pack(pady=(0, 5))
combo_origem = ttk.Combobox(frame, values=moedas, state="readonly", font=("Arial", 10))
combo_origem.set("BRL")
combo_origem.pack(fill="x", pady=(0, 15))

ttk.Label(frame, text="Moeda de destino:", font=("Arial", 10)).pack(pady=(0, 5))
combo_destino = ttk.Combobox(frame, values=moedas, state="readonly", font=("Arial", 10))
combo_destino.set("USD")
combo_destino.pack(fill="x", pady=(0, 20))

btn_converter = ttk.Button(frame, text="Converter", command=converter)
btn_converter.pack(fill="x", pady=(0, 10))

label_resultado = ttk.Label(frame, text="", font=("Arial", 12, "bold"), foreground="#007acc", anchor="center")
label_resultado.pack(fill="x", pady=10)

# Rodar a interface
janela.mainloop()
