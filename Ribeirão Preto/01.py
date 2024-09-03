def fibonacci_sequence(n):
    fibonacci_numbers = [0, 1]
    while fibonacci_numbers[-1] < n:
        next_value = fibonacci_numbers[-1] + fibonacci_numbers[-2]
        fibonacci_numbers.append(next_value)
    return fibonacci_numbers

def is_in_fibonacci(n):
    sequence = fibonacci_sequence(n)
    if n in sequence:
        return f"O número {n} pertence à sequência de Fibonacci."
    else:
        return f"O número {n} NÃO pertence à sequência de Fibonacci."

numero = int(input("Informe um número para verificar se pertence à sequência de Fibonacci: "))

resultado = is_in_fibonacci(numero)
print(resultado)
