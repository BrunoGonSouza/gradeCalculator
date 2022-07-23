'''Universidade Cruzeiro do sul
    Bruno gonçalves de souza
    05/05/22
    25 – Escreva uma expressão que será utilizada para
    decidir se um aluno foi ou não aprovado. Para ser
    aprovado, todas as médias do aluno devem ser maiores
    que 7. Considere que o aluno cursa apenas três
    matérias, e que a nota de cada uma está armazenada
    nas seguintes variáveis: materia1, materia2, materia3.'''



materia1 = float(input("Digite a média da matéria 1: "))

materia2 = float(input("Digite a média da matéria 2: "))

materia3 = float(input("Digite a média da matéria 3: "))

if (materia1 >= 7 and materia2 >= 7 and materia3 >= 7):
    print("Aluno aprovado")
else:
    if (materia1 < 7 and materia2 < 7 and materia3 < 7):
        reprovado = "matéria 1, materia 2 e matéria 3"
    elif (materia1 < 7 and materia2 < 7):
        reprovado = "matéria 1 e materia 2"
    elif (materia2 < 7 and materia3 < 7):
        reprovado = "matéria 2 e materia 3"
    elif (materia1 < 7 and materia3 < 7):
        reprovado = "matéria 1 e materia 3"
    elif (materia1 < 7):
        reprovado = "matéria 1"
    elif (materia2 < 7):
        reprovado = "matéria 2"
    elif (materia3 < 7):
        reprovado = "matéria 3"
        
    print(f"Aluno em recuperação por causa de {reprovado}")
    
  
    




