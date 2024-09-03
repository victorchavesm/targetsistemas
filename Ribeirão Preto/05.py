# Simulação das lâmpadas e interruptores
interruptores = ["Interruptor 1", "Interruptor 2", "Interruptor 3"]
lampadas = ["Lâmpada 1", "Lâmpada 2", "Lâmpada 3"]

# Estado inicial das lâmpadas (todas apagadas e frias)
estado_lampadas = {
    "Lâmpada 1": {"ligada": False, "quente": False},
    "Lâmpada 2": {"ligada": False, "quente": False},
    "Lâmpada 3": {"ligada": False, "quente": False}
}

# Passo 1: Ligar o primeiro interruptor e esperar
estado_lampadas["Lâmpada 1"]["ligada"] = True
estado_lampadas["Lâmpada 1"]["quente"] = True  # Simulando que a lâmpada ficou quente

# Passo 2: Desligar o primeiro interruptor e ligar o segundo
estado_lampadas["Lâmpada 1"]["ligada"] = False
estado_lampadas["Lâmpada 2"]["ligada"] = True

# Passo 3: Verificar o estado das lâmpadas
for lampada, estado in estado_lampadas.items():
    if estado["ligada"]:
        print(f"{lampada} está ligada e corresponde ao Interruptor 2")
    elif estado["quente"]:
        print(f"{lampada} está apagada mas quente e corresponde ao Interruptor 1")
    else:
        print(f"{lampada} está apagada e fria e corresponde ao Interruptor 3")
