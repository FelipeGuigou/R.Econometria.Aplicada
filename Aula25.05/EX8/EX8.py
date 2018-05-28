'''

Exercício 8: Calcula e apresenta o custo com energia elétrica.
Autores: Felipe Guigou e Cirillo Stassen
Versão: 0.1
Comentário: Referente a aula de 25/05/2018.

'''

#Entrada de Dados

Consumo = float(input("Digite o consumo de energia elétrica em kWh:"))
Instalacao = input("Digite o tipo de instalação de rede (r se residencial, i se industrial e c se comercial):")

#Processamento de Dados

if Instalacao == 'r':
	if Consumo <= 500:
		a = Consumo*0.4
	else:
		a = Consumo*0.65
elif Instalacao == 'c':
	if Consumo <= 1000:
		a = Consumo*0.55
	else:
		a = Consumo*0.6
else:
	if Consumo <= 5000:
		a = Consumo*0.55
	else:
		a = Consumo*0.6

#Saída

print("O custo da energia elétrica é de R$", a)

