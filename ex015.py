qtdeDias = int(input('Quantos dias você ficou com o carro? '))
qtdeKm = float(input('Quantos km você percorreu com o carro? '))
valTot = (60 * qtdeDias) + (0.15 * qtdeKm)
print('O valor total do aluguel do carro é de R${:.2f} reais'.format(valTot))