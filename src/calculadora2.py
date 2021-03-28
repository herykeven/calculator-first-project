#Complete as funcoes a seguir

def soma(a, b):
	return "Soma é: ", a+b

def subtrai(a, b):
	return "Subtração é: ", a-b

def multiplica(a, b):
	return "Multiplicação é: ", a*b

def divide(a, b):
        if (b == 0):
            return "Não pode dividir por zero!"
        else:
            return "O resultado da divisão é: ", a / b
	


#Programa principal
	

print("Calculadora simples")

num1 = float(input("Insira o primeiro numero: "))
num2 = float(input("Insira o segundo numero: "))

print(soma(num1, num2))
print(subtrai(num1, num2))
print(multiplica(num1, num2))
print(divide(num1, num2))

print(":)")