# Conversor de Moedas 💱

Um aplicativo desktop simples e eficiente para conversão de moedas em tempo real, construído com Python e Tkinter. O aplicativo utiliza a API pública [Frankfurter](https://www.frankfurter.app/) para obter as taxas de câmbio mais recentes.

## Funcionalidades

- Interface gráfica amigável e fácil de usar.
- Conversão em tempo real entre várias moedas populares (USD, EUR, BRL, GBP, JPY, AUD, CAD).
- Tratamento de erros de conexão e de entradas inválidas.

## Pré-requisitos

Certifique-se de ter o Python instalado na sua máquina (versão 3.6 ou superior).

## Como Instalar e Executar

1. Clone o repositório ou faça o download dos arquivos.
2. Navegue até o diretório do projeto no terminal:
   ```bash
   cd conversor-moedas
   ```
3. Instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
   ```
4. Execute o aplicativo:
   ```bash
   python converter.py
   ```

## Tecnologias Utilizadas

- **Python**: Linguagem principal.
- **Tkinter/ttk**: Para a construção da interface gráfica (built-in do Python).
- **Requests**: Para realizar requisições HTTP para a API de taxas de câmbio.
- **Frankfurter API**: API open-source para dados de câmbio estrangeiros.

## Possíveis Melhorias Futuras

- Adicionar suporte a mais moedas.
- Mostrar histórico de conversões ou gráfico de variação de taxa.
- Alternância para tema escuro.
