# Criando um dicionário para armazenar os alunos
alunos = {}

# Criando a função “situacao_aluno” para calcular média das notas, porcentagem de frequência, se o aluno tem muitas faltas e se o aluno foi aprovado ou reprovado. criando as variáveis para calcular essas situações.
def situacao_aluno(notas, frequencia, carga_horaria):

    # Calculando a média das notas do aluno.
    media = sum(notas) / len(notas) if notas else 0

    # Calculando a porcentagem de frequência.
    porcentagem_frequencia = (frequencia / carga_horaria) * 100

    # Verificando se o aluno foi reprovado por falta de acordo com os 75% solicitado na questão.
    if porcentagem_frequencia < 75:
        return "Reprovado por Falta"

    # Verificando se o aluno foi aprovado ou reprovado por nota (média).
    elif media >= 7:
        return "Aprovado"
    else:
        return "Reprovado por Nota"

# Função para adicionar um aluno
def adicionar_aluno(nome):

    # Adicionando o aluno ao dicionário com notas (dentro de uma lista) e frequência iniciais.
    alunos[nome] = {"notas": [], "frequencia": 0}

# Função para editar o nome do aluno, caso seja necessário.
def editar_aluno(nome_antigo, nome_novo):

    # Verifica se o aluno existe
    if nome_antigo in alunos:

        # Transferindo informações para o novo nome (utilizando o método pop remover o nome antigo do aluno e substituir pelo nome novo).
        alunos[nome_novo] = alunos.pop(nome_antigo)

# Função para remover o nome de um aluno.
def remover_aluno(nome):

    # Remover o aluno, se existir.
    if nome in alunos:
        del alunos[nome]

# Função para adicionar notas.
def adicionar_notas(nome, notas):

    # Adiciona até 4 notas ao aluno existente, assim como pedido na atividade.
    if nome in alunos and len(alunos[nome]["notas"]) < 4:
        alunos[nome]["notas"].extend(notas)

# Função para adicionar frequência.
def adicionar_frequencia(nome, aulas):

    # Adicionando a frequência ao aluno indicado.
    if nome in alunos:
        alunos[nome]["frequencia"] += aulas

# Função para imprimir relatório geral.
def imprimir_relatorio(carga_horaria):

    # Imprime cada aluno com suas informações.
    for nome, info in alunos.items():
        situacao = situacao_aluno(info["notas"], info["frequencia"], carga_horaria)

        # Calculando a média e printando.
        media = sum(info["notas"]) / len(info["notas"]) if info["notas"] else 0
        print(f"{nome} - nota: {media:.1f} / frequência: {info['frequencia']} aulas - ({situacao})")

# Função para imprimir relatório específica (filtro).
def imprimir_relatorio_filtrado(carga_horaria, filtro):

    # Imprimindo apenas os alunos com a situação filtrada
    for nome, info in alunos.items():
        situacao = situacao_aluno(info["notas"], info["frequencia"], carga_horaria)
        if situacao == filtro:

            # Calcula a média para exibição
            media = sum(info["notas"]) / len(info["notas"]) if info["notas"] else 0
            print(f"{nome} - nota: {media:.1f} / frequência: {info['frequencia']} aulas - ({situacao})")

# Solicitando a carga horária da disciplina (primeira mensagem que será solicitada ao usuário.
carga_horaria = int(input("Informe a carga horária da disciplina: "))

# Menu principal do sistema (loop principal).
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

    # Solicitando uma opção ao usuário.
    opcao = input("Escolha uma opção: ")

    if opcao == '1':  # Adiciona o Aluno
        nome = input("Informe o nome do aluno: ")
        adicionar_aluno(nome)
        print(f"Aluno {nome} adicionado com sucesso!")

    elif opcao == '2':  # Edita o nome do Aluno
        nome_antigo = input("Informe o nome do aluno a ser editado: ")
        nome_novo = input("Informe o novo nome do aluno: ")
        editar_aluno(nome_antigo, nome_novo)
        print(f"Aluno {nome_antigo} editado para {nome_novo} com sucesso!")

    elif opcao == '3':  # Remove um Aluno
        nome = input("Informe o nome do aluno a ser removido: ")
        remover_aluno(nome)
        print(f"Aluno {nome} removido com sucesso!")

    elif opcao == '4':  # Adiciona as Notas
        nome = input("Informe o nome do aluno: ")
        notas = list(map(float, input("Informe as notas separadas por espaço: ").split()))
        adicionar_notas(nome, notas[:4])  # Adiciona apenas até 4 notas
        print(f"Notas adicionadas ao aluno {nome} com sucesso!")

    elif opcao == '5':  # Adiciona Frequência
        nome = input("Informe o nome do aluno: ")
        aulas = int(input("Informe a quantidade de aulas frequentadas: "))
        adicionar_frequencia(nome, aulas)
        print(f"Frequência adicionada ao aluno {nome} com sucesso!")

    elif opcao == '6':  # Imprime Relatório Geral
        print("\nRelatório Geral:")
        imprimir_relatorio(carga_horaria)

    elif opcao == '7':  # Imprime Relatório Específico/Filtrado
        situacao_filtro = input("Informe a situação para filtrar (Aprovado, Reprovado por Falta, Reprovado por Nota): ")
        print("\nRelatório Filtrado:")
        imprimir_relatorio_filtrado(carga_horaria, situacao_filtro)

    elif opcao == '0':  # Sair
        print("Saindo do sistema...")
        break

    else:  # Em caso de opção inválida
        print("Opção inválida! Favor, escolher uma das opções disponíveis.")