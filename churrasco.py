print("Bem-vindo ao assistente para churrasco!")

# Solicita ao usuário o número de homens, mulheres e crianças
num_homem = int(input("Digite o número de homens: "))
num_mulher = int(input("Digite o número de mulheres: "))
num_crianca = int(input("Digite o número de crianças: "))

# Define as quantidades de carne necessárias para cada tipo de pessoa, 
# partindo do pressuposto que todos vao comer frango e pao de alho
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


# define os preços KG
# Define os preços por kg de cada tipo de carne
preco_carne = {
    "Picanha": 40.0,
    "Alcatra": 30.0,
    "Fraldinha": 25.0,
    "Linguiça": 15.0,
    "Frango": 20.0
}

# Mostra as opções de carne ao usuário
print("\nEscolha o tipo de carne que deseja:")
print("1 - Picanha")
print("2 - Alcatra")
print("3 - Fraldinha")
print("4 - Linguiça")
print("5 - Frango")

# Pede ao usuário que escolha o tipo de carne
opcao_carne = int(input())

# Verifica a escolha do usuário e calcula o custo da carne
if opcao_carne == 1:
    custo_carne = quantidade_carne * preco_carne["Picanha"]
    tipo_carne = "Picanha"
elif opcao_carne == 2:
    custo_carne = quantidade_carne * preco_carne["Alcatra"]
    tipo_carne = "Alcatra"
elif opcao_carne == 3:
    custo_carne = quantidade_carne * preco_carne["Fraldinha"]
    tipo_carne = "Fraldinha"
elif opcao_carne == 4:
    custo_carne = quantidade_carne * preco_carne["Linguiça"]
    tipo_carne = "Linguiça"
elif opcao_carne == 5:
    custo_carne = quantidade_frango * preco_carne["Frango"]
    tipo_carne = "Frango"
else:
    print("Opção inválida. Escolha novamente.")
    # Adicione aqui uma lógica para lidar com a opção inválida ou encerrar o programa, se necessário.


# quantidades de bebidas por pessoa
cerveja_por_homem = 2  # litros de cerveja
cerveja_por_mulher = 1
refrigerante_por_crianca = 0.5
agua_por_pessoa = 1

# calcula a quantidade total de bebidas 
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

# Define os preços por litro de cada tipo de bebida
preco_bebida = {
    "Cerveja": 8.00,
    "Refrigerante": 4.00,
    "Água": 2.50
}

print("\nEscolha o tipo de bebida que deseja:")
print("1 - Cerveja")
print("2 - Refrigerante")
print("3 - Água")
print("4 - Finalizar escolha de bebidas")

while True:
    opcao_bebida = int(input())
    if opcao_bebida == 1:
        quantidade_cerveja += 1
    elif opcao_bebida == 2:
        quantidade_refrigerante += 1
    elif opcao_bebida == 3:
        quantidade_agua += 1
    elif opcao_bebida == 4:
        break

custo_carne = quantidade_carne * preco_carne[tipo_carne]

custo_bebida = (
    quantidade_cerveja * preco_bebida["Cerveja"]
    + quantidade_refrigerante * preco_bebida["Refrigerante"]
    + quantidade_agua * preco_bebida["Água"]
)

custo_total = custo_carne + custo_bebida

# imprime na tela as informações
print("\nResumo do churrasco:")
print("Quantidade de carne: {:.2f} kg de {}".format(quantidade_carne, tipo_carne))
print("Quantidade de frango: {:.2f} kg".format(quantidade_frango))
print("Quantidade de pão de alho: {}".format(quantidade_pao_de_alho))
print("Quantidade de cerveja: {} litros".format(quantidade_cerveja))
print("Quantidade de refrigerante: {} litros".format(quantidade_refrigerante))
print("Quantidade de água: {} litros".format(quantidade_agua))
print("Custo total do churrasco: R$ {:.2f}".format(custo_total))
