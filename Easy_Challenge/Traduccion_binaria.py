"""
Created on Fri nov 15 13:35:09 2022

@author: Diegodepab
"""
#FUNCIONES capacez  de pasar de binario a decimal y viceversa

def decimal_a_binario(n):
    binario = ""
    while n > 0:
        binario = str(n % 2) + binario
        n = n // 2
    return binario #si quisiera devolverlo en int()

def decimal_a_binario_automatico(n):  #version str
    return int(bin(n).replace("0b", ""))

def binario_a_decimal(b):
    b = str(b)
    decimal = 0
    for i in range(len(b)):
        potencia = len(b) - (i + 1)
        decimal += int(b[i]) * (2 ** potencia)
    return decimal #int

def binario_a_decimal_automatico(b): #version str
    return int(str(b), 2)

# Prueba de las funciones
print(decimal_a_binario(50))  # Numero decimal a binario

print(binario_a_decimal(1010))  # Numero binario a decimal

#en caso de decimal a hexadecimal: hex(num_decimal)

#de hexadecimal a decimal: int('0xff', 16)

