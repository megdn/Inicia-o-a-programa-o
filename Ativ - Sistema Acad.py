# Criando um dicionário para armazenar os alunos
alunos = {}

# Criando a função “situacao_aluno” para calcular média das notas, porcentagem de frequência, se o aluno tem muitas faltas e se o aluno foi aprovado ou reprovado. criando as variáveis para calcular essas situações.
def situacao_aluno(notas, frequencia, carga_horaria):
    if len(notas) > 0:

# Calculando a média das notas do aluno, verificando se a lista de notas está vazia
        media = sum(notas) / len(notas) 
    else:
        media = 0

# Calculando a porcentagem de frequência.
    porcentagem_frequencia = (frequencia / carga_horaria) * 100

 # Verificando se o aluno foi reprovado por falta de acordo com os 75% solicitado na questão
    if porcentagem_frequencia < 75:
        return "Reprovado por Falta"
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado por Nota"

# Função para adicionar um aluno
def adicionar_aluno(nome):
    alunos[nome] = {"notas": [], "frequencia": 0}
    print(f"Aluno {nome} adicionado com sucesso!")

# Função para editar o nome do aluno
def editar_aluno(nome_antigo, nome_novo):
    if nome_antigo in alunos:
        alunos[nome_novo] = alunos[nome_antigo]
        del alunos[nome_antigo]
        print(f"Aluno {nome_antigo} editado para {nome_novo} com sucesso!")
    else:
        print(f"Aluno {nome_antigo} não encontrado!")

# Função para remover um aluno
def remover_aluno(nome):
    if nome in alunos:
        del alunos[nome]
        print(f"Aluno {nome} removido com sucesso!")
    else:
        print(f"Aluno {nome} não encontrado!")

# Função para adicionar notas. O código verifica se o aluno já possui 4 notas, se já existir ele não permite inserir mais notas. Após esta verificação, se aprovada, é utilizado o método “.extend” para inserir a nota.
def adicionar_notas(nome, notas):
    if nome in alunos:
        if len(alunos[nome]["notas"]) < 4:
            alunos[nome]["notas"].extend(notas)
            print(f"Notas adicionadas ao aluno {nome} com sucesso!")
        else:
            print(f"O aluno {nome} já possui 4 notas.")
    else:
        print(f"Aluno {nome} não encontrado!")

# Função para adicionar frequência. Caso o aluno seja encontrado, será inserido a quantidade de aulas que o aluno esteve presente.
def adicionar_frequencia(nome, aulas):
    if nome in alunos:
        alunos[nome]["frequencia"] += aulas
        print(f"Frequência adicionada ao aluno {nome} com sucesso!")
    else:
        print(f"Aluno {nome} não encontrado!")

# Função para imprimir relatório geral. Primeiro verifica se existe aluno inseridos. Se houver, serão listados os alunos e suas respectivas frequências e situação (aprovado ou reprovado). 
def imprimir_relatorio(carga_horaria):
    if not alunos:
        print("Nenhum aluno cadastrado.")
        return
    for nome in alunos:
        info = alunos[nome]
        situacao = situacao_aluno(info["notas"], info["frequencia"], carga_horaria)
        #somando os elementos da lista de notas / tamanho da lista (quantidade de notas inseridas), para fazer a média
        media = sum(info["notas"]) / len(info["notas"]) if len(info["notas"]) > 0 else 0
        print(f"{nome} - nota: {media:.1f} / frequência: {info['frequencia']} aulas - ({situacao})")

# Função para imprimir relatório filtrado
def imprimir_relatorio_filtrado(carga_horaria, filtro):
    #Esta variável será usada para verificar se pelo menos um aluno que corresponde ao filtro
    encontrado = False
    for nome in alunos:
        info = alunos[nome]
        situacao = situacao_aluno(info["notas"], info["frequencia"], carga_horaria)
        if situacao == filtro:
            encontrado = True
            media = sum(info["notas"]) / len(info["notas"]) if len(info["notas"]) > 0 else 0
            print(f"{nome} - nota: {media:.1f} / frequência: {info['frequencia']} aulas - ({situacao})")
    if not encontrado:
        print(f"Nenhum aluno encontrado com a situação '{filtro}'.")

# Solicitando a carga horária da disciplina. Será a primeira mensagem que o usuário verá na tela.
print("Sabendo que a carga horária é dada em dias.")
carga_horaria = int(input("Informe a carga horária: "))

# Menu principal do sistema
while True:
    print("\nMenu:")
    print("1. Adicionar Aluno")
    print("2. Editar Aluno")
    print("3. Remover Aluno")
    print("4. Adicionar Notas")
    print("5. Adicionar Frequência")
    print("6. Imprimir Relatório Geral")
    print("7. Imprimir Relatório Filtrado")
    print("0. Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Informe o nome do aluno: ")
        adicionar_aluno(nome)

    elif opcao == '2':
        nome_antigo = input("Informe o nome do aluno a ser editado: ")
        nome_novo = input("Informe o novo nome do aluno: ")
        editar_aluno(nome_antigo, nome_novo)

    elif opcao == '3':
        nome = input("Informe o nome do aluno a ser removido: ")
        remover_aluno(nome)

    #As notas do aluno são inseridas separadas por espaço e com o método ".split" são separadas como elementos de uma lista.
    #Utilizei a função "map()" para aplicar a função "float" a cada item da lista criada pelo ".split".
    #Para converter o resultado do "map" para uma string utilizei a função "list".
    elif opcao == '4':
        nome = input("Informe o nome do aluno: ")
        notas = list(map(float, input("Informe as notas separadas por espaço: ").split()))
        adicionar_notas(nome, notas[:4])  # Adiciona até 4 notas como solicitado.

    elif opcao == '5':
        nome = input("Informe o nome do aluno: ")
        aulas = int(input("Informe a quantidade de aulas frequentadas: "))
        adicionar_frequencia(nome, aulas)

    elif opcao == '6':
        print("\nRelatório Geral:")
        imprimir_relatorio(carga_horaria)

    elif opcao == '7':
        situacao_filtro = input("Informe a situação para filtrar (Aprovado, Reprovado por Falta, Reprovado por Nota): ")
        print("\nRelatório Filtrado:")
        imprimir_relatorio_filtrado(carga_horaria, situacao_filtro)

    elif opcao == '0':
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida! Favor, escolher uma das opções disponíveis.")
