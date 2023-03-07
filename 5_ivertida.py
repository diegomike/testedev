# 5) Escreva um programa que inverta os caracteres de um string.

# IMPORTANTE:
# a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código;
# b) Evite usar funções prontas, como, por exemplo, reverse;

# Define a string a ser invertida
string_original = "target sistemas"

# Inicializa a string invertida como vazia
string_invertida = ""

#  Aqui utilizei o "for" que percorre a string original de trás para frente, começando na última posição "(len(string_original) - 1)" e indo até a 
# primeira posição (0), decrementando de um em um "(-1)" a cada iteração.
# Dentro do loop, adicionei cada caractere na string invertida usando o operador de concatenação (+).
for i in range(len(string_original) - 1, -1, -1):
    string_invertida += string_original[i]

# Exibe as strings original e o resultado da string invertida
print("String original:", string_original)
print("String invertida:", string_invertida)