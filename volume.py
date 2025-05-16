def calcular_volume_retangular(comprimento, largura, altura):
  volume = comprimento * largura * altura
  return volume

comprimento = 12
largura = 14
altura = 20

volume_calculado = calcular_volume_retangular(comprimento, largura, altura)

print(f"O volume da caixa retangular é: {volume_calculado} cm³")