# FIBONACCI

# Escribe un programa que imprima los 10 primeros numero de la sucesión de fibonacci empezando en 0.
# La serie fibonacci se compone por una sucesión de numeros en la que el siguiente siempre es la suma de los dos anteriores.
# 0, 1, 1, 2, 3, 5, 8, 13,...

a, b = 0, 1

for i in range(10):
    print(a)
    c = a + b
    a = b
    b = c