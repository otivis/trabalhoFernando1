print("Bem-vindo ao assistente para churrasco!")

# Solicita ao usuário o número de homens, mulheres e crianças
num_homem = int(input("Digite o número de homens: "))
num_mulher = int(input("Digite o número de mulheres: "))
num_crianca = int(input("Digite o número de crianças: "))

# Define as quantidades de carne necessárias para cada tipo de pessoa,
# partindo do pressuposto que todos vão comer frango e pão de alho
carne_por_homem = 0.5  # kg de carne
carne_por_mulher = 0.4
carne_por_crianca = 0.2
frango_por_pessoa = 0.3
pao_de_alho_por_pessoa = 1

# Calcula a quantidade total de carne necessária
quantidade_carne = (
    num_homem * carne_por_homem
    + num_mulher * carne_por_mulher
    + num_crianca * carne_por_crianca
)
quantidade_frango = (
    num_homem * frango_por_pessoa
    + num_mulher * frango_por_pessoa
    + num_crianca * frango_por_pessoa
)
quantidade_pao_de_alho = (
    num_homem * pao_de_alho_por_pessoa
    + num_mulher * pao_de_alho_por_pessoa
    + num_crianca * pao_de_alho_por_pessoa
)

# Define os preços por kg
preco_carne = {
    "Picanha": 40.0,
    "Alcatra": 30.0,
    "Fraldinha": 25.0,
    "Linguiça": 15.0,
    "Frango": 20.0
}

# Inicializa a lista de carnes escolhidas pelo usuário
carnes_escolhidas = []

# Mostra as opções de carne ao usuário
print("\nEscolha o tipo de carne que deseja (digite o número da opção e pressione Enter):")
print("1 - Picanha")
print("2 - Alcatra")
print("3 - Fraldinha")
print("4 - Linguiça")
print("5 - Frango")
print("6 - Finalizar escolha de carnes")

# Pede ao usuário que escolha o tipo de carne
while True:
    opcao_carne = input()
    if opcao_carne == "1":
        carnes_escolhidas.append(("Picanha", preco_carne["Picanha"]))
    elif opcao_carne == "2":
        carnes_escolhidas.append(("Alcatra", preco_carne["Alcatra"]))
    elif opcao_carne == "3":
        carnes_escolhidas.append(("Fraldinha", preco_carne["Fraldinha"]))
    elif opcao_carne == "4":
        carnes_escolhidas.append(("Linguiça", preco_carne["Linguiça"]))
    elif opcao_carne == "5":
        carnes_escolhidas.append(("Frango", preco_carne["Frango"]))
    elif opcao_carne == "6":
        break

cerveja_por_homem = 2  # litros
cerveja_por_mulher = 1
refrigerante_por_crianca = 0.5
agua_por_pessoa = 1

# Calcula a quantidade total de bebidas necessária
quantidade_cerveja = (
    num_homem * cerveja_por_homem
    + num_mulher * cerveja_por_mulher
)
quantidade_refrigerante = num_crianca * refrigerante_por_crianca
quantidade_agua = (
    num_homem * agua_por_pessoa
    + num_mulher * agua_por_pessoa
    + num_crianca * agua_por_pessoa
)

# Define os preços por litro
preco_bebida = {
    "Cerveja": 8.0,
    "Refrigerante": 4.0,
    "Água": 2.5
}

# Inicializa as quantidades de bebida em zero
quantidade_cerveja = 0
quantidade_refrigerante = 0
quantidade_agua = 0

# Mostra as opções de bebida ao usuário
print("\nEscolha o tipo de bebida que deseja (digite o número da opção e pressione Enter):")
print("1 - Cerveja")
print("2 - Refrigerante")
print("3 - Água")
print("4 - Finalizar escolha de bebidas")

# Pede ao usuário que escolha o tipo de bebida
while True:
    opcao_bebida = input()
    if opcao_bebida == "1":
        quantidade_cerveja += 1
    elif opcao_bebida == "2":
        quantidade_refrigerante += 1
    elif opcao_bebida == "3":
        quantidade_agua += 1
    elif opcao_bebida == "4":
        break

# Calcula o custo total da carne
custo_carne = sum([carne[1] for carne in carnes_escolhidas]) * quantidade_carne

# Calcula o custo total das bebidas
custo_bebida = (
    quantidade_cerveja * preco_bebida["Cerveja"]
    + quantidade_refrigerante * preco_bebida["Refrigerante"]
    + quantidade_agua * preco_bebida["Água"]
)

# Calcula o custo total do churrasco
custo_total = custo_carne + custo_bebida

# Imprime na tela as informações
print("\nResumo do churrasco:")
print("Quantidade de carne: {:.2f} kg".format(quantidade_carne))
print("Quantidade de frango: {:.2f} kg".format(quantidade_frango))
print("Quantidade de pão de alho: {}".format(quantidade_pao_de_alho))
print("Quantidade de cerveja: {} litros".format(quantidade_cerveja))
print("Quantidade de refrigerante: {} litros".format(quantidade_refrigerante))
print("Quantidade de água: {} litros".format(quantidade_agua))
print("Custo total do churrasco: R$ {:.2f}".format(custo_total))
