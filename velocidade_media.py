import matplotlib.pyplot as plt
import numpy as np

# Definir dados
tempo = np.array([0, 3, 6, 9, 11, 14])  # tempo em segundos
distancia = np.array([0, 2, 4, 6, 8, 10])  # distancia em metros

# Calcular velocidade média
velocidade = np.diff(distancia) / np.diff(tempo)


# Criar gráfico de velocidade média
plt.plot(tempo[1:], velocidade)
plt.xlabel('Tempo (s)')
plt.ylabel('Velocidade (m/s)')
plt.title('Gráfico de Velocidade Média')
plt.show()
