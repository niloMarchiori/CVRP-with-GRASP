import numpy as np
import matplotlib.pyplot as plt
import os
np.random.seed(42)
tempo = np.random.uniform(0, 100, 10000)  # Simulando tempos aleatórios de eventos
valores = np.random.normal(50, 10, 10000)  # Valores associados ao evento

# Criar figura
fig, ax = plt.subplots(figsize=(10, 5))

# Criar hexbin plot (melhor para muitos pontos)
hb = ax.hexbin(tempo, valores, gridsize=50, cmap='inferno', mincnt=1)

# Adicionar barra de cores
plt.colorbar(hb, label="Densidade de Pontos")

# Configurações
ax.set_xlabel("Tempo")
ax.set_ylabel("Valor do Evento")
ax.set_title("Distribuição de Densidade dos Eventos")

# Salvar o gráfico
plt.savefig("heatmap_eventos.png", dpi=300)
plt.show()