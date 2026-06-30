import requests

def converter(valor, moeda_origem, moeda_destino):
    url = f"https://api.frankfurter.app/latest?amount={valor}&from={moeda_origem}&to={moeda_destino}"
    resposta = requests.get(url)
    if resposta.status_code != 200:
        return "Erro ao acessar API"
    dados = resposta.json()
    return dados["rates"][moeda_destino]

if __name__ == "__main__":
    print("Conversor de Moedas 💱")
    valor = float(input("Digite o valor: "))
    origem = input("Moeda de origem (ex: BRL): ").upper()
    destino = input("Moeda de destino (ex: USD): ").upper()

    resultado = converter(valor, origem, destino)
    print(f"{valor} {origem} = {resultado:.2f} {destino}")
