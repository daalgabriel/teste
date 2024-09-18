'''2) Escreva um programa que verifique, em uma string, a existência da letra (a)
, seja maiúscula ou minúscula, além de informar a quantidade de vezes em que ela ocorre.'''

def verificar_a(texto):

    #mudar toda a string para minusculo para contar tudo.
    texto = texto.lower()

    #contar o número de vezes que a letra 'A' aparece na string. 
    numero_vezes_aparece = texto.count('a')

    existe_a = numero_vezes_aparece > 0

    return existe_a, numero_vezes_aparece

#input pelo usuário
texto = str(input("Digite uma string: \n"))

ocorrencia, numero_vezes_aparece = verificar_a(texto)

if ocorrencia is True: 
    print(f"A letra 'A' aparece {numero_vezes_aparece} vezes na string. ")
else:
    print(f"A letra 'A' NÃO aparece na string. ")