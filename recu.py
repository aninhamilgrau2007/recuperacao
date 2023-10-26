class TaskManager:
    def __init__(self):
        self.tasks = {}

    def add_task(self, description):
        task_id = len(self.tasks) + 1
        self.tasks[task_id] = description
        return f"Tarefa adicionada {task_id}"

    def list_tasks(self):
        if not self.tasks:
            return "Não existem tarefas ainda"
        tasks_list = [f"{task_id} - {description}" for task_id, description in self.tasks.items()]
        return "\n".join(tasks_list)

    def update_task(self, task_id, new_description):
        if task_id in self.tasks:
            self.tasks[task_id] = new_description
            return "Tarefa atualizada"
        else:
            return "Tarefa não existe"

    def delete_task(self, task_id):
        if task_id in self.tasks:
            del self.tasks[task_id]
            return "Tarefa deletada com sucesso"
        else:
            return "Tarefa não encontrada"

def main():
    task_manager = TaskManager()

    while True:
        print("1 - Adicionar tarefa")
        print("2 - Ler tarefa")
        print("3 - Atualizar tarefa")
        print("4 - Deletar tarefa")
        print("5 - Sair")

        opcao = input("Digite uma opção: ")

        if opcao == "1":
            tarefa = input("Digite a tarefa:")
            result = task_manager.add_task(tarefa)
            print(result)

        elif opcao == "2":
            tasks = task_manager.list_tasks()
            print(tasks)

        elif opcao == "3":
            chave = int(input("Digite o número da tarefa que deseja atualizar: "))
            if chave in task_manager.tasks:
                nova_tarefa = input("Digite a nova descrição da tarefa: ")
                result = task_manager.update_task(chave, nova_tarefa)
                print(result)
            else:
                print("Tarefa não encontrada")

        elif opcao == "4":
            chave = int(input("Digite o número da tarefa que deseja deletar: "))
            if chave in task_manager.tasks:
                result = task_manager.delete_task(chave)
                print(result)
            else:
                print("Tarefa não foi encontrada na lista")

        elif opcao == "5":
            print("O programa se encerrou.")
            break

        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
