# Entrada de Dados
a = float(input("Digite sua velocidade em quilômetros por hora:"))

#Processamento
if a > 80:
	b = (a-80)*5
	print("Você levou uma multa por excesso de velocidade, sua multa tem valor (em reais) de:", b)	
else: 
	print("Você não levou uma multa por excesso de velocidade, mantenha sua prudência no trânsito!")
