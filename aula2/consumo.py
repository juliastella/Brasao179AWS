distancia_percorrida_km = 300
combustivel_gasto_litros = 25 


consumo_medio_kml = distancia_percorrida_km / combustivel_gasto_litros

print("Detalhes da Viagem:")
print(f"  Distância Percorrida: {distancia_percorrida_km:.2f} km") 
print(f"  Combustível Gasto:    {combustivel_gasto_litros:.2f} litros") 
print("-" * 30) 
print(f"Consumo Médio:        {consumo_medio_kml:.2f} km/l")