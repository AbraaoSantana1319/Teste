print('_'*30)

print('Sequência de Fibonacci')

print('_'*30)

n = int(input('Insira um numero para gerar a sequência de Fibonnaci: '))

num1 = 0

num2 = 1

print('-'*30)

print('{} -> {}'.format(num1, num2), end = '')

cont = 3

while cont <= n:

   num3 = num1 + num2

   print('-> {}'.format(num3), end = '')

   num1 = num2

   num2 = num3

   cont += 1

