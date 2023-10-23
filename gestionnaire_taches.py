import json

class Task:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = []
    

# Exemple d'utilisation de la classe Task
if __name__ == "__main__":
    task_manager = Task('tasks.json')
    task_manager.load_tasks_from_file()

    while True:
        print("\nMenu:")
        print("1. Ajouter une tâche")
        print("2. Afficher les tâches")
        print("3. Quitter")

        choice = input("Choisissez une option : ")

        if choice == '1':
            description = input("Entrez la description de la tâche : ")
            due_date = input("Entrez la date limite (YYYY-MM-DD) : ")
            is_completed = False  # Par défaut, la tâche n'est pas terminée
            task_manager.add_task(description, due_date, is_completed)
        elif choice == '2':
            task_manager.list_tasks()
        elif choice == '3':
            break
        else:
            print("Option invalide. Veuillez réessayer.")

    print("Application de gestion de tâches terminée.")
