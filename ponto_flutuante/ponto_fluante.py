# Definindo 0.1 para a variável e vendo como ela se comporta quando aumentamos suas casas decimais
x = 0.1
print(x) 
print(f'{x:.10f}') #imprime com formato com 10 casas decimais
print(f'{x:.20f}') #imprime com formato com 20 casas decimais

# Quando definimos 20 casas decimais, percebe-se que as últimas três casas aparecem com 555, mas por quê?
# Isso ocorre porque nem todos os decimais possuem uma representação binária, o que ocasiona em uma representação não exata

print(0.1 + 0.1 + 0.1 == 0.3) # Não possui representação binária, então mesmo matematicamente estando correto, seu armazenamento retorna outro valor
print(0.5 + 0.5 + 0.5 == 1.5) # Possui representação binária

# Algumas maneiras que podemos fazer para contornar esse problema
# 1-) Fazer a diferença e comparar com uma certa tolerância
tolerância = 1e-10
print(abs(0.1 + 0.1 + 0.1 - 0.3) < tolerância)

# 2-) Arredondar ambos os lados após os cálculos
print(round(0.1 + 0.1 + 0.1, 10) == round(0.3, 10))

# O ponto flutuante define a precisão, ou seja, a quantidade de memória
# Podemos ter precisão simples (32 bits), precisão dupla (64 bits), etc.

# A representação dupla é separada da seguinte maneira:
# 1 bit --> sinal
# 11 bits --> expoente
# 53 bits --> mantissa

# Exemplo: 0.012 (1.2 * 10^-2)
# Sinal = +
# Expoente = -2
# Mantissa = 1.1

import struct

def binary(num):
    return ''.join('{:0>8b}'.format(c) for c in struct.pack('!d', num))

def print_binary(num):
    bin = binary(num)
    print(bin[0], bin[1:12], bin[13:])

# Potências de 2
print_binary(0.5) 
print_binary(1.0)
print_binary(2.0)
print_binary(-2.0)

# Potências de 10
print_binary(0.1)
print_binary(0.01)
print_binary(-0.1)

# As mantissas de potência 10 são todas dízimas, enquanto as de potência 2 são todas 0
# 53 bits de mantissa equivalem a aproximadamente 15/16 dígitos decimais