'''

Arquivo: Exercicio3.py
Versão: 0.0.1
Data: 19/05/2018
Autor: Felipe Guigou
Comentários: Toma uma velocidade em quilômetros por hora e define se o motorista leva uma multa, se a multa é devida, diz o valor da multa.

'''
# Entrada de Dados
a = float(input("Digite sua velocidade em quilômetros por hora:"))

#Processamento
b = (a-80)*5

#Saída
if a > 80:
	print("Você levou uma multa por excesso de velocidade, sua multa tem valor de", b, "reais (R$).")	
else: 
	print("Você não levou uma multa por excesso de velocidade, mantenha sua prudência no trânsito!")
