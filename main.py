def verifica_fibonacci(numero):
    a, b = 0, 1
    
    if numero == 0 or numero == 1:
        return True
    
    while b <= numero:
        if b == numero:
            return True
            
        a, b = b, a + b
    return False

numero = int(input("Digite um número para verificar se ele pertence à sequência de Fibonacci: "))

if verifica_fibonacci(numero):
    print(f"O número {numero} pertence à sequência de Fibonacci.")
else:
    print(f"O número {numero} não pertence à sequência de Fibonacci.")
