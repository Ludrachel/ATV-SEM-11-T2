conceito=0
while conceito==0:
    nota_aluno = float(input())

    if nota_aluno < 0 or nota_aluno > 10:
        print("Nota inválida.")
        continue
    
    if nota_aluno >= 8.5:
        conceito = "A"
        break
    elif nota_aluno >= 7.0:
        conceito = "B"
        break
    elif nota_aluno >= 5.0:
        conceito = "C"
        break
    elif nota_aluno >= 4.0:
        conceito = "D"
        break
    elif nota_aluno >= 0:
        conceito = "E"
        break
    

print(conceito)


        
