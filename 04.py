def next_element(sequence):
    if sequence == 'a':
        # Sequência: 1, 3, 5, 7, ___
        # Lógica: Incrementa de 2 em 2
        return 7 + 2
    elif sequence == 'b':
        # Sequência: 2, 4, 8, 16, 32, 64, ____
        # Lógica: Multiplica por 2
        return 64 * 2
    elif sequence == 'c':
        # Sequência: 0, 1, 4, 9, 16, 25, 36, ____
        # Lógica: Quadrado dos números naturais (n^2)
        return (len([0, 1, 4, 9, 16, 25, 36]))**2
    elif sequence == 'd':
        # Sequência: 4, 16, 36, 64, ____
        # Lógica: Quadrado dos números pares (2n)^2
        return (len([4, 16, 36, 64]) * 2)**2
    elif sequence == 'e':
        # Sequência: 1, 1, 2, 3, 5, 8, ____
        # Lógica: Sequência de Fibonacci
        fib = [1, 1, 2, 3, 5, 8]
        return fib[-1] + fib[-2]
    elif sequence == 'f':
        # Sequência: 2, 10, 12, 16, 17, 18, 19, ____
        # Lógica: Parece que a sequência adiciona números de forma não linear, mas com um padrão de incrementos menores após um grande incremento inicial
        # 2 (inicial)
        # 10 (2 + 8)
        # 12 (10 + 2)
        # 16 (12 + 4)
        # 17 (16 + 1)
        # 18 (17 + 1)
        # 19 (18 + 1)
        # Se continuarmos com esse padrão de adicionar 1, o próximo número seria:
        # 19 + 1 = 20
        return 20

# Imprime os próximos elementos de cada sequência
print(f"a) {next_element('a')}")
print(f"b) {next_element('b')}")
print(f"c) {next_element('c')}")
print(f"d) {next_element('d')}")
print(f"e) {next_element('e')}")
print(f"f) {next_element('f')}")
