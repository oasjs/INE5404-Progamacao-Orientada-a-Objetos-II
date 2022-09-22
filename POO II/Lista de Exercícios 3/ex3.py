'''Escreva um programa que lê duas notas de vários alunos e armazena tais
notas em um dicionário, onde a chave é o nome do aluno. A entrada de dados deve
terminar quando for lida uma string vazia como nome. Escreva uma função que retorna
a média do aluno, dado seu nome.'''

student_dict = {}
while True:

    student = str(input("Insira o nome do aluno: "))
    if student == "":
        break
    grades = input("Insira suas notas: ").split()
    for i in range(len(grades)):
        grades[i] = float(grades[i])

    student_dict.update({student:grades})

def get_average(student):
    return f'A média de {student} é {round(sum(student_dict[student]) / len(student_dict[student]), 2)}'

print(student_dict)
print(get_average(input("Digite o nome de um aluno na lista: ")))   