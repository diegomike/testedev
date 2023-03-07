# Insere o número que deseja que seja calculado a sequência em fibonacci
num = int(input("Digite um número: "))

# Calcula a sequência de Fibonacci em um laço de repetição até o número informado
fib = [0, 1]
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])
    
 # Imprime a sequência de Fibonacci em uma única linha utilizando uma expressão convertedora para converter cada numero da sequencia em string 
 # Nesse caso utilizei a expressão "str(i) for i in fib" para criar uma lista de strings contendo a representação em texto de cada
 # número da lista fib.
 
print("Sequência de Fibonacci:", ", ".join(str(i) for i in fib))

# Verifica se o número informado pertence à sequência fibonacci ou não e imprime a sequencia na tela
if num in fib:
    print(f"{num} pertence à sequência de Fibonacci.")
else:
    print(f"{num} não pertence à sequência de Fibonacci.")