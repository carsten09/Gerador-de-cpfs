"""
Primeiro desafio
"""

numero = int(input('Digite um número inteiro: '))

if numero % 2 == 0:
    print('Par')
else:
    print('Impar')


horario = input('Digite um horario (0-23):')

if horario.isdigit():
    horario = int(horario)

    if horario < 0 or horario > 23:
        print('Horário deve ser entre 0-23')
    else:
        if horario <= 11:
            print('Bom dia')
        elif horario <= 17:
            print('Boa tarde')
        else:
            print('Boa noite')
else:
    print('Por favor digie um horario entre 0 e 23')
    
    


nome = input('Digite seu primeiro nome:')
tamanho = len(nome)

if tamanho <= 4:
    print('Seu nome é curto')
elif tamanho <=6:
    print('Seu nome é normal')
else:
    print('Seu nome é muito grande')


















