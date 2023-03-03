fibo = int(input('Digite o número desejado: '))

a, b = 0, 1

while a < fibo:
    a, b = b, a + b

print(a == fibo)