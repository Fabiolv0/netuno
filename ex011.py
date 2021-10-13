alturaParede = float(input('Diga a altura da parede: '))
larguraParede = float(input('Diga a largura da parede: '))
areaParede = alturaParede * larguraParede
litrosTinta = areaParede / 2
print('A área total da parede é de {:.2f} metros quadrados e será necessário usar {:.2f} litros de tinta para pintá-la'.format(areaParede, litrosTinta))