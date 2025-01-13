import numpy as np
import matplotlib.pyplot as plt


massa_carrinho_adicional_g = np.array([0, 10, 20, 30, 40, 50, 60])  
massa_carrinho_base_g = 230  
massa_gancho_kg = 20 / 1000  
aceleracao_m_s2 = np.array([0.954, 0.917, 0.902, 0.868, 0.836, 0.800, 0.774])


massa_total_kg = (massa_carrinho_base_g + massa_carrinho_adicional_g) / 1000
inverso_massa_total = 1 / massa_total_kg


plt.figure(figsize=(8, 6))
plt.scatter(inverso_massa_total, aceleracao_m_s2, color='blue', label='Dados experimentais')
plt.xlabel('1/Massa total (1/kg)')
plt.ylabel('Aceleração (m/s²)')
plt.title('Gráfico de Aceleração x 1/Massa Total')

# Ajuste linear 
coef_angular, coef_linear = np.polyfit(inverso_massa_total, aceleracao_m_s2, 1)
reta_tendencia = coef_angular * inverso_massa_total + coef_linear
plt.plot(inverso_massa_total, reta_tendencia, color='red', label=f'Reta de tendência (Inclinação = {coef_angular:.2f})')


plt.legend()
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

# Comparacao
forca_resultante = massa_gancho_kg * 9.8
print(f"Inclinação da reta de tendência: {coef_angular:.2f} N")
print(f"Força resultante aplicada: {forca_resultante:.3f} N")
