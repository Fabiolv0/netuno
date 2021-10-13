precoAtual = float(input('Qual o preço atual do produto? '))
precoNovo = precoAtual - (precoAtual * 0.05)
print('O produto que custava R${}, com o desconto de 5%, agora custa R${:.2f} reais'.format(precoAtual, precoNovo))