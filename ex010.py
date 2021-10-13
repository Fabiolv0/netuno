qtdeReal = float(input('Diga quanto de reais você tem: R$'))
convertToDolar = qtdeReal / 3.27
print('Com R${:.2f} reais, você consegue comprar U${:.2f} dólares'.format(qtdeReal, convertToDolar))