import time
listaDeTarefas = []

while True:
    print("O que você quer fazer:\n".upper())
    print("1. Adicionar tarefa")
    print("2. executar tarefa")
    print('3. sair\n')

    op = int(input("Digite sua opção: "))

    if op == 1:
        tarefa = input("Digite a descrição da tarefa: ")
        listaDeTarefas.append(tarefa)

    elif op == 2:
        print(f"Excutando: {listaDeTarefas.pop(0)}\n")

    elif op == 3:
        print("Saindo...")
        time.sleep(2)
        break

    else:
        print("Operação inexistente")