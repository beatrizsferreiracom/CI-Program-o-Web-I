# 2) Faça um programa que leia 4 notas de um aluno, salve as em uma lista e calcule a média das notas.

nomeAluno = input("Insira o nome do aluno: ")

notaMatematica = input("Nota em matemática: ")
notaPortugues = input("Nota em Potuguês: ")
notaHistoria = input("Nota em História: ")
notaGeografia = input("Nota em Geografia: ")

totalNotas = float(notaMatematica) + float(notaPortugues) + float(notaHistoria) + float(notaGeografia)

mediaNotas = float(totalNotas) / 4

print("A média de " + nomeAluno + " foi de " + str(mediaNotas))
