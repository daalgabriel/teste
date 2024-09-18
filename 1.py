'''1) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
 (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, 
 ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.'''


# Função para verificar se o numéro(x) pertence ou não a sequência de fibonnaci
def fibo(x):
    if x < 0:

        #Se o número informado for negativo, ele já informa false, porque números negativos não fazem parte da fibo.
        return False
    
    #A sequência fibo começa com [0, 1] como foi informado na questão
    sequecia_fibo = [0, 1]

    # Gerar a sequência até que o número seja maior ou igual ao número informado
    while sequecia_fibo[-1] < x:
        sequecia_fibo.append(sequecia_fibo[-1] + sequecia_fibo[-2])

    return x in sequecia_fibo

#input pelo usuário
numero = int(input("Informe um número: \n"))

pertence_fibo = fibo(numero)

if pertence_fibo is True:
    print(f"O número {numero} pertence à sequência de Fibonnaci.")
else:
    print(f"O número {numero} NÃO pertence à sequência de Fibonnaci.")
