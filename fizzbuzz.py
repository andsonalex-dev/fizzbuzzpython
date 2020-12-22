from random import randint

def fizzbuzz(numero):
    if numero % 3 == 0:
        return f'fizz, {numero} é divisivel por 3'
    if numero % 5 == 0:
        return f'buzz, {numero} é divisivel por 5'
    if numero % 3 == 0 and numero % 5 == 0:
        return f'fizzbuzz, {numero} é divisivel por 3 e 5'
    return numero
    

for i in range(100):
    aleatorio = randint(0, 100)
    print(fizzbuzz(aleatorio))
