def calcular_preco_total(nome_produto, preco_unitario, quantidade):
  preco_total = preco_unitario * quantidade
  mensagem = f"Produto: {nome_produto}\n"
  mensagem += f"Preço unitário: R$ {preco_unitario:.2f}\n"
  mensagem += f"Quantidade: {quantidade}\n"
  mensagem += f"Preço total: R$ {preco_total:.2f}"
  return mensagem

# Informações da compra
nome_do_produto = "Cadeira Infantil"
preco = 12.40
quantidade_comprada = 3

# Calcula e exibe o preço total
detalhes_da_compra = calcular_preco_total(nome_do_produto, preco, quantidade_comprada)
print(detalhes_da_compra)