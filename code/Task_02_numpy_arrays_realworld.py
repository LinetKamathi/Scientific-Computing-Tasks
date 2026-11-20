# REAL-WORLD CASE: Greenhouse monitoring on a farm in Thika
# Assumptions: 24 hourly temperature (C) and relative humidity (%) readings from
# IoT sensors. Crops are stressed when temperature > 30 C or humidity > 85 %.
import numpy as np

temp_c = np.array([16.5, 16.0, 15.8, 15.5, 16.2, 18.0, 21.0, 25.0, 28.5, 31.0, 33.2, 34.5,
                   35.0, 34.2, 32.8, 30.5, 28.0, 25.5, 22.5, 20.0, 18.8, 17.9, 17.2, 16.8])
humidity = np.array([88, 89, 90, 91, 90, 86, 78, 68, 60, 52, 48, 45,
                     44, 46, 50, 55, 63, 72, 80, 84, 86, 87, 88, 88], dtype=float)

print(f"Mean temperature: {temp_c.mean():.2f} C  | Max: {temp_c.max():.1f} C at hour {temp_c.argmax()}")
print(f"Mean humidity: {humidity.mean():.1f} %  | Min: {humidity.min():.0f} %")

heat_stress = temp_c > 30
humid_stress = humidity > 85
print("Hours of heat stress:", heat_stress.sum())
print("Hours of high humidity:", humid_stress.sum())
print("Hours when BOTH occur:", (heat_stress & humid_stress).sum())

temp_k = temp_c + 273.15           # vectorized Celsius -> Kelvin
print("First four temperatures in Kelvin:", temp_k[:4])
