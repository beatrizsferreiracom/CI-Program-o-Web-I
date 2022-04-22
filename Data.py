#Desenvolva um programa Python que devolva leia um nome e uma data e retorne uma String.

nome = input("Digite seu nome: ")
dia = input("Digite o dia: ")
mês = input("Digite o mês: ")
ano = input("Digite o ano: ")

PrimeiraLetraNome = nome[0:1]
ContinuaçãoNome = nome[1: ]

nascimento = "{}{} nasceu no dia: {}/{}/{}"

print(nascimento.format(PrimeiraLetraNome.upper(), ContinuaçãoNome.lower(), dia, mês, ano))
