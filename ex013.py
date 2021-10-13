salario = float(input('Qual o salário do funcionário? R$'))
novoSalario = salario + (salario * 0.15)
print('O funcionário que ganhava R${}, com 15% de aumento, passa a ser R${:.2f} reais'.format(salario, novoSalario))