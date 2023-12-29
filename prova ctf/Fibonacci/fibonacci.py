# Função definida para calcular o valor da sequência
def fibon(n):
    if n <= 0: # Testa se o numero é menor ou igual a zero, e apresenta uma mensagem caso seja
        return "O valor de n deve ser um número inteiro positivo."

    # aqui testa e retorna o para 1 e 1 para 2  
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibon(n - 1) + fibon(n - 2)

# Função principal para execução geral 
def main():
    # Bloco try-except usado para melhor prevenção de "Exceções" que possa vir causar algum tipo de erro
    try: # Int já aplicado para uso de numeros inteiros, sem precisar de conversão futura
        n = int(input("Digite um número inteiro positivo (n): "))
        resultado = fibon(n)
        print(f"O {n}-ésimo valor da sequência de Fibonacci é: {resultado}")
    except ValueError:
        print("Por favor, insira um número inteiro positivo válido.")

if __name__ == "__main__":
    main()
