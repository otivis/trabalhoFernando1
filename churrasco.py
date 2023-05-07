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
preco_picanha = 40.0
preco_alcatra = 30.0
preco_fraldinha = 25.0
preco_linguica = 15.0
preco_frango = 20.0

# Mostra as opções de carne ao usuário
print("\nEscolha o tipo de carne que deseja:")
print("1 - Picanha")
print("2 - Alcatra")
print("3 - Fraldinha")
print("4 - Linguiça")

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
else:
    custo_carne = quantidade_frango * preco_carne["Frango"]
    tipo_carne = "Frango"


#  os preços de cada tipo de bebida  litro
preco_bebida = {
    "Cerveja": 8.00,
    "Refrigerante": 4.00,
    "Água": 2.50
}

# inicializa as quantidades de bebida em zero
quantidade_cerveja = 0
quantidade_refrigerante = 0
quantidade_agua = 0

# mostra as opções de bebida 
print("\nEscolha o tipo de bebida que deseja:")
print("1 - Cerveja")
print("2 - Refrigerante")
print("3 - Água")
print("4 - Finalizar escolha de bebidas")

# solicita ao usuário a escolha de bebida e calcula a quantidade
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
print("Quantidade de cerveja: {}".format(quantidade_cerveja))
print("Quantidade de refrigerante: {}".format(quantidade_refrigerante))
print("Quantidade de água: {}".format(quantidade_agua))
print("Custo total do churrasco: R$ {:.2f}".format(custo_total))
