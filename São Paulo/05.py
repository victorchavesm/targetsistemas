def inverter_string(s):
    invertida = ""
    for i in range(len(s) - 1, -1, -1):
        invertida += s[i]
    return invertida

string_original = input("Digite uma string para inverter: ")

string_invertida = inverter_string(string_original)
print(f"String original: {string_original}")
print(f"String invertida: {string_invertida}")
