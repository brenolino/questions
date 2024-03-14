############## Questão 1: ##############
print("Questão 1.")

indice = 13
soma = 0
k = 0

while k < indice:
    k += 1
    soma += k

print(f"Valor da soma é: {soma}")

########################################

############## Questão 2: ##############
print("\nQuestão 2.")

numero = input("Digite um número: ")
numero = int(numero)
a, b = 0, 1

while b < numero:
    a, b = b, a + b

if b == numero:
    print(numero, "pertence à sequência de Fibonacci! :)")

else:
    print(numero, "não pertence à sequência de Fibonacci! :(")

########################################

############## Questão 3: ##############
print("\nQuestão 3.")

print("a) 9")
print("b) 128")
print("c) 49")
print("d) 100")
print("e) 13")
print("f) 20")

########################################

############## Questão 4: ##############

# Eu ligo o interruptor 1 e espero por um tempo, então desligo e ligo o interruptor 2. Então, vou para o quarto 1, se a lampada estiver apagada e quente, ela é do interruptor 1, se estiver acesa é do interruptor 2 e se estiver apagada e fria é do interruptor 3, depois vou para o quarto 2 e sigo a mesma lógica, por exclusão eu saberei qual é o interruptor do quarto 3. 

########################################

############## Questão 5: ##############
print("\nQuestão 5.")

palavra = input("Digite uma palavra para invertê-la: ")
palavraInversa = ""

for i in range(len(palavra) - 1, -1, -1):
    palavraInversa += palavra[i]

print(f"O inverso de {palavra} é {palavraInversa}.")