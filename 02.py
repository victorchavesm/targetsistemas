def verificar_letra_a(string):
    count = string.lower().count('a')
    
    if count > 0:
        return f"A letra 'a' (maiúscula ou minúscula) ocorre {count} vezes na string."
    else:
        return "A letra 'a' (maiúscula ou minúscula) não foi encontrada na string."

entrada = input("Digite uma string: ")

resultado = verificar_letra_a(entrada)
print(resultado)
