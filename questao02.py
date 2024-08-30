def fibonacci(num):
    fib1 = 0
    fib2 = 1

    if num < 0:
        return False

    while fib1 < num:
        novo_fib2 = fib1 + fib2
        fib1 = fib2
        fib2 = novo_fib2

    return fib1 == num

numero = int(input())

if fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci")

