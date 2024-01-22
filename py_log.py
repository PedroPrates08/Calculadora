#Calculadora simples com participação direta do usuário

#Valores para o usuário poder escrever 
valor1 = int(input("Digite seu número: "))
condicao = input("Digite sua condiçao: ")
valor2 = int(input("Digite seu outro número: "))


#Condições de sinais matemáticos 
if condicao == "+":
    op = valor1 + valor2

elif condicao == "-":
    op = valor1 - valor2

elif condicao == "*":
    op = valor1 * valor2

elif condicao == "/":
    op = valor1 / valor2

else:
    print("condiçao invalida")

print(op)
