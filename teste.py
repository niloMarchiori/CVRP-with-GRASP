
import pandas as pd

# Criando um DataFrame com uma célula contendo múltiplas linhas
data = {
    "Coluna1": ["Linha1\nLinha2\nLinha3"],
    "Coluna2": ["Outro valor"]
}

df = pd.DataFrame(data)
df.to_csv("out.csv", index=False)