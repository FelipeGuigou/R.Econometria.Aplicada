# Entrada de Dados
a = float(input("Digite sua velocidade em quilômetros por hora:"))

#Processamento
if a > 120:
	b = (a-120)*5
#Saída
	print("Você levou uma multa por excesso de velocidade, sua multa tem valor (em reais) de:", b)	
else: 
	print("Você não levou uma multa por excesso de velocidade, mantenha sua prudência no trânsito!")
