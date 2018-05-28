'''

Arquivo: Exercicio4.py
Versão: 0.0.1
Data: 19/05/2018
Autor: Felipe Guigou
Comentários: Toma os coeficientes de uma função quadrática, calcula e apresenta sua(s) raíz(es).

'''
#Entrada de Dados
a = float(input("Digite o número que multiplica x ao quadrado:"))
b = float(input("Digite o número que multiplica x:"))
c = float(input("Digite o número que será a constante:"))

#Processamento
x = (b**2)-(4*a*c)
y = x**0.5
x1 = (-b+y)/(2*a)
x2 = (-b-y)/(2*a)

#Saída
if x<0 :
	print("Delta negativo, raízes inexistem")
elif x1 == x2 :
	print("Raíz única, de valor:", x1)
else :
	print("A primeira raíz da função é:", x1)
	print("A segunda raíz da função é:", x2)
