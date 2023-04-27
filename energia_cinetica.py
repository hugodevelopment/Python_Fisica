import matplotlib.pyplot as plt

massa = float(input("Insira a massa do objeto em Kg: "))

velocidades = list(range(0,50,2))
print(velocidades)

energias_cineticas = [0.5 * massa * v**2 for v in velocidades]

plt.plot(velocidades,energias_cineticas)
plt.xlabel("Velocidades m/s")
plt.ylabel("Energia Cinetica Joules")
plt.title("Relação entre velocidade e energia cinética")
plt.show()