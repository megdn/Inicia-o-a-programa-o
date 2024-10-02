print(“\nBEM VINDO(A) À SUA LISTA DE TAREFAS!”)

def mostrar_menu():
    print("\n====== LISTA DE TAREFAS ======")
    print("1. Adicionar Nova Tarefa")
    print("2. Ver Lista")
    print("3. Excluir Tarefa")
    print("4. Recuperar Tarefa")
    print("5. Pesquisar Tarefa")
    print("6. Editar Tarefa")
    print("7. Sair")

def carregar_tarefas(arquivo):
    try:
        with open(arquivo, 'r') as f:
            return [linha.strip() for linha in f.readlines()]
    except FileNotFoundError:
        return []

def salvar_tarefas(tarefas, arquivo):
    with open(arquivo, 'w') as f:
        for tarefa in tarefas:
            f.write(f"{tarefa}\n")

def adicionar_tarefa(tarefas):
    nova_tarefa = input("Digite a descrição da nova tarefa: ")
    tarefas.append(nova_tarefa)
    print("Tarefa adicionada com sucesso!")

def ver_tarefas(tarefas):
    if not tarefas:
        print("\nLista de tarefas vazia.")
    else:
        print("\nLista de Tarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa}")

def excluir_tarefa(tarefas, tarefas_excluidas):
    ver_tarefas(tarefas)
    try:
        indice = int(input("Digite o número da tarefa que deseja excluir: "))
        if 1 <= indice <= len(tarefas):
            tarefas_excluidas.append(tarefas.pop(indice - 1))
            print("Tarefa excluída com sucesso!")
        else:
            print("Número de tarefa inválido.")
    except ValueError:
        print("Entrada inválida. Digite um número correspondente à tarefa que deseja excluir.")

def recuperar_tarefa(tarefas, tarefas_excluidas):
    if not tarefas_excluidas:
        print("\nNão há tarefas excluídas para recuperar.")
    else:
        print("\nTarefas Excluídas:")
        for i, tarefa in enumerate(tarefas_excluidas, start=1):
            print(f"{i}. {tarefa}")
        try:
            indice = int(input("Digite o número da tarefa que deseja recuperar: "))
            if 1 <= indice <= len(tarefas_excluidas):
                tarefas.append(tarefas_excluidas.pop(indice - 1))
                print("Tarefa recuperada com sucesso!")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número correspondente à tarefa que deseja recuperar.")

def pesquisar_tarefa(tarefas):
    if not tarefas:
        print("\nLista de tarefas vazia.")
    else:
        try:
            indice = int(input("\nDigite o número da tarefa que deseja pesquisar: "))
            if 1 <= indice <= len(tarefas):
                print(f"Tarefa encontrada: {tarefas[indice - 1]}")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número correspondente à tarefa que deseja pesquisar.")

def editar_tarefa(tarefas):
    if not tarefas:
        print("\nLista de tarefas vazia. Não há tarefas para editar.")
    else:
        try:
            indice = int(input("\nDigite o número da tarefa que deseja editar: "))
            if 1 <= indice <= len(tarefas):
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                tarefas[indice - 1] = nova_tarefa
                print("Tarefa editada com sucesso!")
            else:
                print("Número de tarefa inválido.")
        except ValueError:
            print("Entrada inválida. Digite um número correspondente à tarefa que deseja editar.")

def main():
    tarefa_salvas_tarefas = "tarefas.txt"
    tarefa_salvas_tarefas_excluidas = "tarefas_excluidas.txt"
    tarefas = carregar_tarefas(tarefa_salvas_tarefas)
    tarefas_excluidas = carregar_tarefas(tarefa_salvas_tarefas_excluidas)
    while True:
        mostrar_menu()
        escolha = input("Escolha uma opção: ")
        if escolha == '1':
            adicionar_tarefa(tarefas)
        elif escolha == '2':
            ver_tarefas(tarefas)
        elif escolha == '3':
            excluir_tarefa(tarefas, tarefas_excluidas)
        elif escolha == '4':
            recuperar_tarefa(tarefas, tarefas_excluidas)
        elif escolha == '5':
            pesquisar_tarefa(tarefas)
        elif escolha == '6':
            editar_tarefa(tarefas)
        elif escolha == '7':
            print("Saindo...")
            salvar_tarefas(tarefas, tarefa_salvas_tarefas)
            salvar_tarefas(tarefas_excluidas, tarefa_salvas_tarefas_excluidas)
            break
        else:
            print("Opção inválida. Por favor, escolha uma das opções indicadas.")

if __name__ == "__main__":
    main()
