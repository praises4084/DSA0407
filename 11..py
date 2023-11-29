import numpy as np
fuel_efficiency = np.array([25, 30, 28, 35, 32, 27, 29])

average_fuel_efficiency = np.mean(fuel_efficiency)
print("Average fuel efficiency:", average_fuel_efficiency)

index_model_A = 0  
index_model_B = 3  

fuel_efficiency_model_A = fuel_efficiency[index_model_A]
fuel_efficiency_model_B = fuel_efficiency[index_model_B]

percentage_improvement = ((fuel_efficiency_model_B - fuel_efficiency_model_A) / fuel_efficiency_model_A) * 100

print(f"Fuel efficiency of Model A: {fuel_efficiency_model_A} mpg")
print(f"Fuel efficiency of Model B: {fuel_efficiency_model_B} mpg")
print(f"Percentage improvement between Model A and Model B: {percentage_improvement:.2f}%")
