opcao = -1
while True:
    
    if opcao != 0:
        print('OPÇÕES:')
        print('1 - SAUDAÇÃO')
        print('2 - BRONCA')
        print('3 - FELICITAÇÃO')
        print('0 - FIM')

    opc = int(input())

    if opc == 1:
        print('1 - Olá. Como vai?')

    elif opc == 2:
        print('2 - Vamos estudar mais.')

    elif opc == 3:
        print('3 - Meus Parabéns!')

    elif opc != 0:
        print('Opção inválida.')

    if opc == 0:
        break

print('0 - Fim de serviço.')
