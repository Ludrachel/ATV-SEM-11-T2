
valor_total = 0
qtd = 0
while True:

    if valor_total != "X":
        print("""CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA""")

    codigo = input().upper()[0]

    if codigo == "X":
        break
    elif codigo == "H":
        valor_total += 5.50
    
    elif codigo == "C":
        valor_total += 6.80
        
    elif codigo == "M":
        valor_total += 4.50
        
    elif codigo == "A":
        valor_total += 7.00
        
    elif codigo == "Q":
        valor_total += 4.00
     
    else:
        print('Opção inválida.')
        continue
    
    
    

print(f'{valor_total:.2f}')
