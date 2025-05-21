# 1- Conversor de Moeda

# Taxas de câmbio
dolar_taxa = 5.20
euro_taxa = 6.15

# Pergunta ao usuário qual conversão deseja
conversao_escolhida = int(input("Para qual moeda você quer converter?\n1 - Dólar\n2 - Euro\nEscolha: "))

# Pergunta o valor em reais
valor_em_reais = float(input("Qual o valor em reais que você quer converter? R$: "))

# Realiza a conversão e exibe o resultado
if conversao_escolhida == 1:
    valor_convertido = valor_em_reais / dolar_taxa
    print(f"R$ {valor_em_reais:.2f} é equivalente a US$ {valor_convertido:.2f}")
elif conversao_escolhida == 2:
    valor_convertido = valor_em_reais / euro_taxa
    print(f"R$ {valor_em_reais:.2f} é equivalente a € {valor_convertido:.2f}")
else:
    print("Opção inválida. Por favor, escolha 1 para Dólar ou 2 para Euro.")