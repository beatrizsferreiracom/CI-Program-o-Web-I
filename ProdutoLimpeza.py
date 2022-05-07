# 1) Faça um algoritmo que ajude uma empresa de limpeza. Para isso o programa deve ler a largura
# e o comprimento de um cômodo e calcular e mostrar a área a ser limpa e a quantidade de produto
# necessária para o serviço, sabendo que cada litro de produto limpa uma área de 2 metros quadrados.


largura = input("Largura em m²: ")
comprimento = input("Comprimento em m²: ")

area = float(largura) * float(comprimento)

quantidadeProduto = float(area) / 2

print( "Serão necessários " + str(quantidadeProduto) + " litros do produto para o serviço.")
