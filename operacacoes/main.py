# -*- coding: utf-8 -*-

'''from avancados.operacoes import soma

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))

resultado = soma(a, b)

print(f"A soma de {a} e {b} é: {resultado} ")'''

'''def verificar(texto):

    if texto.startswith("Olá"):
        print("A sua frase começa com um 'Olá'.")
    else:
        print("A sua frase não começa com um 'Olá'.")

frase = input("Digite uma frase: ")
verificar(frase)'''

'''def criar_arquivo():

    texto = input("Insira um texto: ")

    with open('texto.txt', 'w', encoding='utf-8')as arquivo:
        arquivo.write(texto)
    print("Arquivo criado com sucesso!")

criar_arquivo()'''

'''from avancados.multiplicar import*
from avancados.subtrair import*
from avancados.verificar_par import*

a = float(input("Insira o valor de a: "))
b = float(input("Insira o valor de b: "))
c = float(input("Insira o valor de c: "))
d = float(input("Insira o valor de d: "))

numero = int(input("Insira um número para a verificar se ele é par: "))
if verificar_par(numero):
    print(f"O número {numero} digitado é par!")
else:
    print(f"O número {numero} digitado é não par! ")

total = multiplicar(a, b)
resultado = subtrair(c, d)

print(f"A multiplicação de {a} e {b} é: {total} ")
print(f"A subtração de {c} e {d} é: {resultado} ")'''

'''def somar_multiplos_de_tres(numeros):
    try:
        with open(numeros, 'r') as arquivo:
            soma = 0
            for linha in arquivo:
                try:
                    numero = int(linha.strip())
                    if numero % 3 == 0:
                        soma += numero
                except ValueError:
                    continue  
            return soma
    except FileNotFoundError:
        print(f"Erro: O arquivo '{numeros}' não foi encontrado.")
        return 0


arquivo_existente = 'numeros.txt


resultado = somar_multiplos_de_tres(arquivo_existente)
print(f"A soma dos múltiplos de 3 é: {resultado}")'''

'''with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    palavras = arquivo.read().split()

with open('palavras_filtradas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(f"{palavra}\n" for palavra in palavras if palavra.lower().startswith('b') and palavra.lower().endswith('o'))

print("As palavras foram filtradas e salvas em 'palavras_filtradas.txt'.")'''

'''with open('palavras.txt', 'r', encoding='utf-8' ) as arquivo:
    for linha in arquivo:
        if linha.strip().endswith('a'):
            print(linha.strip())'''

'''from avancados.divisao import dividir

def processar_arquivo():
    try:
        with open('valores.txt', 'r') as arquivo:
            linhas = arquivo.readlines()

        for linha in linhas:
            try:
                numero = float(linha.strip())
                resultado = dividir(numero, 2)
                print(f"{numero} ÷ 2 = {resultado}")
            except ValueError:
                print(f"Erro: Não foi possível converter '{linha.strip()}' em número.")
    except FileNotFoundError:
        print("Erro: O arquivo 'valores.txt' não foi encontrado.")

processar_arquivo()'''


'''palavras = [input(f"Digite a palavra {i + 1}: ").strip() for i in range(10)]

with open("palavras_a.txt", "w") as arquivo_a, open("demais_palavras.txt", "w", encoding="utf-8") as arquivo_demais:
    for palavra in palavras:
        if palavra.lower().startswith('a'): 
            arquivo_a.write(palavra + "\n")
        else:
            arquivo_demais.write(palavra + "\n")

print("As palavras foram salvas nos arquivos 'palavras_a.txt' e 'demais_palavras.txt'.")'''



'''def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido.")


resultados = []


for i in range(10):
    print(f"\nDivisão {i + 1}:")
    n1 = obter_numero("Digite o número N1: ")
    n2 = obter_numero("Digite o número N2: ")

    try:
        
        resultado = n1 / n2
        resultados.append(f"Divisão {i + 1}: {n1} / {n2} = {resultado:.2f}")
        print(f"Resultado: {resultado:.2f}")
    except ZeroDivisionError:
        
        resultados.append(f"Divisão {i + 1}: Erro: divisão por zero")
        print("Erro: Não é possível dividir por zero.")
    except Exception as e:
        
        resultados.append(f"Divisão {i + 1}: Erro: {str(e)}")
        print(f"Erro inesperado: {str(e)}")

with open("divisao.txt", "w", encoding="utf-8") as arquivo:
    for resultado in resultados:
        arquivo.write(resultado + "\n")

print("\nAs divisões foram salvas no arquivo 'divisao.txt'.")'''


'''def obter_numero(mensagem):
    while True:
        try:
            return float(input(mensagem))
        except ValueError:
            print("Erro: Digite um número válido.")


resultados = []


for i in range(10):
    print(f"\nMultiplicação {i + 1}:")
    n1 = obter_numero("Digite o número N1: ")
    n2 = obter_numero("Digite o número N2: ")

    try:
        
        resultado = n1 * n2
        resultados.append(f"Multiplicação {i + 1}: {n1} * {n2} = {resultado:.2f}")
        print(f"Resultado: {resultado:.2f}")
    except Exception as e:
        
        resultados.append(f"Multiplicação {i + 1}: Erro: {str(e)}")
        print(f"Erro inesperado: {str(e)}")


with open("multiplicados.txt", "w", encoding="utf-8") as arquivo:
    for resultado in resultados:
        arquivo.write(resultado + "\n")

print("\nAs multiplicações foram salvas no arquivo 'multiplicados.txt'.")'''

with open('palavras.txt', 'r', encoding='utf-8') as arquivo:
    palavras = arquivo.read().split()

with open('palavras_filtradas.txt', 'w', encoding='utf-8') as arquivo:
    arquivo.writelines(f"{palavra}\n" for palavra in palavras if palavra.lower().startswith('m') and palavra.lower().endswith('a'))

print("As palavras foram filtradas e salvas em 'palavras_filtradas.txt'.")
















