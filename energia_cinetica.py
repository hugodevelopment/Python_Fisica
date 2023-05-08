import matplotlib.pyplot as plt

# Colocamos um valor para massa
massa = float(input("Insira a massa do objeto em Kg: "))

# Cria uma lista com os valores de velocidade, nesse caso começa do 0, vai até 50 e é de 2 em 2
velocidades = list(range(0,50,2))

# Cria uma lista com os valores de energia cinetica
energias_cineticas = [0.5 * massa * v**2 for v in velocidades]

# Plota o gráfico
plt.plot(velocidades,energias_cineticas)
plt.xlabel("Velocidades m/s")
plt.ylabel("Energia Cinetica Joules")
plt.title("Relação entre velocidade e energia cinética")
plt.show()