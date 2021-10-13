num = int(input('Digite um número para ver sua tabuada: '))
print('-' * 15)
i = 0
while i<= 10:
    print('{} x {} = {}'.format(num, i, (num*i)))
    i += 1
print('-'* 15)