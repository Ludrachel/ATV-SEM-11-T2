qtd_pessoas = 0
soma_idades = 0
media_idades = 0
menor_idade = 0
maior_idade = 0

while True:

    idade = int(input())

    if idade != 0:
        soma_idades += idade
        qtd_pessoas += 1

    if qtd_pessoas == 1:
        menor_idade = idade
        maior_idade = idade

    if idade < menor_idade:
        if idade != 0:
            menor_idade = idade

    if idade > maior_idade:
        maior_idade = idade

    if qtd_pessoas > 0:
        media_idades = soma_idades / qtd_pessoas

    if idade == 0:
        break
    
if qtd_pessoas != 0:
    print(qtd_pessoas)
    print(f'{media_idades:.2f}')
    print(menor_idade)
    print(maior_idade)
