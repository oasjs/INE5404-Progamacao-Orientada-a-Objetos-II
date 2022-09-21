# Exercício 1.​ Faça um Programa que leia um vetor de 5 números inteiros e mostre-os.
ls1 = [1,2,3,4,5]
for num in ls1:
    print(num, end=" ")
print("")

# Exercício 2. ​Faça um Programa que leia um vetor de 10 números reais e mostre-os na ordem inversa.
ls2 = [0,1,2,3,4,5,6,7,8,9]
for num in reversed(ls2):
    print(num, end=" ")
print("")

# Exercício 3. ​Faça um Programa que leia 4 notas, mostre as notas e a média na tela.
grades = [10,4,6,9]
total = 0
for grade in grades:
    total += grade
print(f'The average grade is {total/len(grades)}')
print("")

# Exercício 4. ​Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes foram lidas. Imprima as consoantes.
ls4 = [1,'a','B','c',5,'K','e','O','l','u']
vowels = ['a','e','i','o','u']
out = []
for character in ls4:
    if type(character) == str:
        if character.lower() not in vowels:
            out.append(character)
print(f'{len(out)} consonants were found.')
print("They are: ", end='')
for consonant in out:
    print(consonant, end=", ")
print("")

# Exercício 5. ​Faça um Programa que leia 20 números inteiros e armazene-os num vetor. Armazene os números pares no vetor PAR e os números IMPARES no vetor impar. Imprima os três vetores.
num_ls = [None]*20
even_ls = []
odd_ls = []
for i in range(20):
    n = int(input())
    num_ls[i] = n
    if n%2 == 0: even_ls.append(n)
    else: odd_ls.append(n)

print(num_ls)
print(even_ls)
print(odd_ls)
print("")

# Exercício 6. ​Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num vetor a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
average_ls = []
for i in range(10):
    grades = input().split()
    total = 0
    for grade in grades:
        grade = float(grade)
        total += grade
    avrg = total/4
    average_ls.append(avrg)

num_over_7 = 0
for grade in average_ls:
    if grade >= 7:
        num_over_7 += 1
print(num_over_7)

# Exercício 7. ​Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
ls7 = [2,4,6,8,10]
sum_total = 0
product = 1
for num in ls7:
    sum_total += num
    product *= num
print(sum_total)
print(product)
print("")

# Exercício 8. ​Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a ordem lida.
num_of_people = 2
ages = [None]*num_of_people
heights = [None]*num_of_people
for i in range(num_of_people):
    info = input().split()
    ages[i] = info[0]
    heights[i] = info[1]
ages.reverse()
heights.reverse()
print(ages)
print(heights)
print("")

# Exercício 9. ​Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre a soma dos quadrados dos elementos do vetor.
ls9 = [1,2,3,4,5,6,7,8,9,10]
total = 0
for num in ls9:
    total += num**2
print(total)

# Exercício 10. ​Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos intercalados dos dois outros vetores.
ls10_1 = [1,2,3,4,5,6,7,8,9,10]
ls10_2 = [1.1,2.2,3.3,4.4,5.5,6.6,7.7,8.8,9.9,11]
ls10_result = [None]*(len(ls10_1)+len(ls10_2))
for i in range(len(ls10_result)):
    if i%2 == 0:
        ls10_result[i] = ls10_1[int(i/2)]
    else:
        ls10_result[i] = ls10_2[int(i/2)]
print(ls10_result)