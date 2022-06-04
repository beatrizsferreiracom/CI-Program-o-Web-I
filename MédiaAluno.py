# Crie um sistema flask que receba na sua rota 3 valores. Esses valores são referentes a 3 notas de um aluno.
# O programa deve informar se o aluno foi aprovado ou reprovado. 
# Para que o aluno seja aprovado a média das 3 notas tem que ser maior ou igual a 60 pontos

from flask import Flask

app = Flask(__name__)

@app.route("/mediaNotas/<x>/<y>/<z>")
def mediaNotas(x, y, z):
    soma = float(x) + float(y) + float(z)
    media = soma/3
    if(soma >= 60):
        return "Você foi aprovado"
    else:
        return "Você foi reprovado"
