import math
sen = int(input('Digite o valor de um ângulo para saber o valor do seno: '))
cos = int(input('Digite o valor de um ângulo para saber o valor do cosseno: '))
tan = int(input('Digite o valor de um ângulo para saber o valor da tangente: '))
print('O seno de {} é {:.2f}'.format(sen, math.sin(sen)))
print('O cosseno de {} é {:.2f}'.format(cos, math.cos(cos)))
print('A tangente de {} é {:.2f}'.format(tan, math.tan(tan)))