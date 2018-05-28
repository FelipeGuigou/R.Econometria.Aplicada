'''

Exercício 7: Toma a idade de um veículo e decide se esse é ou não velho.
Autores: Felipe Guigou e Cirillo Stassen
Versão: 0.1
Comentário: Referente a aula de 25/05/2018.

'''

#Entrada de Dados

idadecarro = float(input("Digite a idade do veículo:"))

#Processamento de Dados

testeidade = idadecarro - 3

#Saída

if testeidade < 0:
	print("O veículo é novo!")
elif testeidade == 0:
	print("Amanhã o veículo já será velho.")
else:
	print("O veículo é velho.")

