# Sintaxe básica de uma função em Python
def minha_funcao():
    print("Olá, esta é a minha função!")
    
minha_funcao()

# Função com parâmetros
def saudacao(nome):
    print(f"Olá, {nome}! Bem-vindo(a) à programação em Python.")

saudacao("Alice")
saudacao("Bob")

# Função com parametros e argumentos padrão
def saudacao_com_idade(nome, idade=30):
    print(f"Olá, {nome}! Você tem {idade} anos.")

saudacao_com_idade("Charlie")
saudacao_com_idade("David", 25)

# Função que retorna um valor
def soma(a, b):
    return a + b
resultado = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")
