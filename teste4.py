# Os próximos elementos das sequências são a) 9, b) 128, c) 49, d) 100, e) 13, f) 200.
# Questão 4, letra a):
n = 0
while n < 9:
    n2 = n + 2
    n = n +1
print(n)    

# Questão 4, letra b):
n = 0
while n < 128:
    n2 = n * 2
    n = n +1
print(n)

# Questão 4, letra c):
# c) 0, 1, 4, 9, 16, 25, 36
# Cada número é igual ao anterior acrescido de um número ímpar que segue a sequência 1, 3, 5, 7, 9. 
# Realizando a subtração dos dois últimos números, temos que 36 - 25 = 11. 
# Assim, devemos acrescentar 11 + 2 = 13 ao último número, obtendo 36 + 13 = 49.

# d) 4, 16, 36, 64
# Cada número é igual ao quadrado dos números pares. Com isso, temos que 64 = 8². 
# Então, o próximo número par é 10, e o seu quadrado é 10² = 100.

# e) 1, 1, 2, 3, 5, 8
# Cada número é igual à soma do número atual com o número anterior. 
# Assim, o próximo número é igual a 8 + 5 = 13.

# f) 2, 10, 12, 16, 17, 18, 19
# Sequência formada através de todos os números que iniciam com a letra d. 
# Assim, o próximo número em ordem crescente que inicia com a letra d é 200.


