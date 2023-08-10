bicicleta_andando = False 

contador = 0

while contador < 2:
    if bicicleta_andando:
        print("Pedala.")
        bicicleta_andando = True
    else:
        print("Pedala.")
        bicicleta_andando = False
    
    contador += 1  # Incrementa o contador

print("Duas pedaladas escapa a correia.")