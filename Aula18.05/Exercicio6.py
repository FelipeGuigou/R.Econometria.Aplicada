'''

Arquivo: Exercicio6.py
Versão: 0.0.1
Data: 19/05/2018
Autor: Felipe Guigou
Comentários: Toma uma velocidade em quilômetros por hora, define se o motorista leva uma multa e calcula o valor dessa multa.

'''
# Entrada de Dados
a = float(input("Digite sua velocidade em quilômetros por hora:"))

#Processamento
b = (a-120)*5

#Saída
if a > 120:
	print("Você levou uma multa por excesso de velocidade, sua multa tem valor (em reais) de:", b)	
else: 
	print("Você não levou uma multa por excesso de velocidade, mantenha sua prudência no trânsito!")
